import base64
from Crypto import Random
from Crypto.Cipher import AES
import keyfile

# encrypt_key and iv data should be in str type (e.g. str_IV = '\x41\x69\x72\x50\x6F\x69\x6E\x74\x48\x69\x70\x61\x73\x73\xFF\xFF')
encrypt_key = keyfile.str_encrypt_key
localIV = keyfile.str_IV

str_dummy = '\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
thisistest = "thisisatest"
dummy_seq = [0x00, 0x01]

class AES128Crypto:

    def __init__(self, encrypt_key, iv):
        self.BS = AES.block_size
        self.encrypt_key = encrypt_key[:16].encode(encoding='utf-8', errors='strict')
        self.iv = iv
        self.pad = lambda s: bytes(s + (self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS), 'utf-8')
        self.unpad = lambda s: s[0:-ord(s[-1:])]

    def encrypt(self, data, seq):
        data = self.pad(data)
        encryptIV = self.iv
        encryptIV[-2] = seq[0]
        encryptIV[-1] = seq[1]
        
        cipher = AES.new(self.encrypt_key, AES.MODE_CBC, encryptIV)

        # 암호화시 앞에 iv와 암화화 값을 붙여 인코딩 한다.
        # 디코딩시 앞에서 BS(block_size) 만금 잘라서 iv를 구하고, 이를통해 복호화 한다.
        return base64.b64encode(encryptIV + cipher.encrypt(data)).decode("utf-8")

    def decrypt(self, data, seq):
        data = base64.b64decode(data)

        # encrypt 에서 작업한 것처럼 첫 16바이트(block_size=BS) 를 잘라 iv를 만들고, 그 뒤를 복호화 하고자 하는 메세지로 잘라 만든다.
        decryptIV = self.iv
        decryptIV[-2] = seq[0]
        decryptIV[-1] = seq[1]
        
        encrypted_msg = data[self.BS:]
        cipher = AES.new(self.encrypt_key, AES.MODE_CBC, decryptIV)
        return self.unpad(cipher.decrypt(encrypted_msg)).decode('utf-8')

##############################################################################################################################

if __name__ == "__main__":
    AESagent = AES128Crypto(encrypt_key, localIV)
    res = AESagent.encrypt(thisistest)
    print(res)
    print(AESagent.decrypt(res))