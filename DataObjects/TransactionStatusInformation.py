from DataObjects.GenericDO import GenericDO


class TransactionStatusInformation(GenericDO):
    def __init__(self, msg, tag="9F40", offset=0):
        GenericDO.__init__(self, msg, tag, offset)

    def parse(self, dataType='b'):
        msg = {
            "Offline data authentication was performed": self.value[0] & 0x80 == 0x80,
            "Cardholder verification was performed": self.value[0] & 0x40 == 0x40,
            "Card risk management was performed": self.value[0] & 0x20 == 0x20,
            "Issuer authentication was performed": self.value[0] & 0x10 == 0x10,
            "Terminal risk management was performed": self.value[0] & 0x08 == 0x08,
            "Script processing was performed": self.value[0] & 0x04 == 0x04,
            "RFU (B1b1-b1b2)": format(self.value[0] & 0x03, "02X"),
            "RFU (B2b1-b2b8)": format(self.value[1], "02X")
        }
        return self.strVal, msg
