#include "config.h"

u8 CU2KIOSK_INIT[] = {0x02, 0x00, 0x01, 0x10, 0x00, 0x00, 0x00, 0x00, 0x03};

u8 CU2KIOSK_OBUINFO[] = {0x02, 0x00, 0x01, 0x20, 0x00, 0x08, 
                        0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08,
                        0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08,
                        0x00, 0x00, 0x03};

u8 CU2KIOSK_OBUINFO2[] = {0x02, 0x00, 0x01, 0x20, 0x00, 0x08, 
                        0x10, 0x82, 0x33, 0x04, 0x05, 0x06, 0x47, 0x08,
                        0x11, 0x52, 0x03, 0x94, 0x05, 0x76, 0x07, 0x08,
                        0x00, 0x00, 0x03};