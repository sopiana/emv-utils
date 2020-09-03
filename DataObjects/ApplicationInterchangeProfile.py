from DataObjects.GenericDO import GenericDO


class ApplicationInterchangeProfile(GenericDO):

    def __init__(self, msg, tag="82", offset=0):
        GenericDO.__init__(self, msg, tag, offset)

    def parse(self, dataType='b'):
        msg = {
            "RFU (B1b8)": self.value[0] & 0x80,
            "SDA supported": self.value[0] & 0x40 == 0x40,
            "DDA supported": self.value[0] & 0x20 == 0x20,
            "Cardholder verification supported": self.value[0] & 0x10 == 0x10,
            "Terminal risk management to be performed": self.value[0] & 0x08 == 0x08,
            "Issuer authentication supported": self.value[0] & 0x04 == 0x04,
            "RFU (B1b2)": self.value[0] & 0x02,
            "CDA supported": self.value[0] & 0x01 == 0x01,
            "RFU (B2b1-B1b8)": format(self.value[1], "02X"),
        }
        return self.strVal, msg
