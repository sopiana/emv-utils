from DataObjects.GenericDO import GenericDO


class AdditionalTerminalCapabilities(GenericDO):
    def __init__(self, msg, tag="9F40", offset=0):
        GenericDO.__init__(self, msg, tag, offset)

    def parse(self, dataType='b'):
        msg = {"Cash": self.value[0] & 0x80 == 0x80,
               "Goods": self.value[0] & 0x40 == 0x40,
               "Services": self.value[0] & 0x20 == 0x20,
               "Cashback": self.value[0] & 0x10 == 0x10,
               "Inquiry": self.value[0] & 0x08 == 0x08,
               "Transfer": self.value[0] & 0x04 == 0x04,
               "Payment": self.value[0] & 0x02 == 0x02,
               "Administrative": self.value[0] & 0x01 == 0x01,
               "Cash Deposit": self.value[1] & 0x80 == 0x80,
               "RFU (B2b1-b2b7)": format(self.value[1] & 0x7F, "02X"),
               "Numeric keys": self.value[2] & 0x80 == 0x80,
               "Alphabetic and special characters keys": self.value[2] & 0x40 == 0x40,
               "Command keys": self.value[2] & 0x20 == 0x20,
               "Function keys": self.value[2] & 0x10 == 0x10,
               "RFU (B3b1-b3b4)": format(self.value[2] & 0x0F, "02X"),
               "Print, attendant": self.value[3] & 0x80 == 0x80,
               "Print, cardholder": self.value[3] & 0x40 == 0x40,
               "Display, attendant": self.value[3] & 0x20 == 0x20,
               "Display, cardholder": self.value[3] & 0x10 == 0x10,
               "RFU (B4b3-b4b4)": format(self.value[3] & 0x0C, "02X"),
               "Code table 10": self.value[3] & 0x02 == 0x02,
               "Code table 9": self.value[3] & 0x01 == 0x01,
               "Code table 8": self.value[4] & 0x80 == 0x80,
               "Code table 7": self.value[4] & 0x40 == 0x40,
               "Code table 6": self.value[4] & 0x20 == 0x20,
               "Code table 5": self.value[4] & 0x10 == 0x10,
               "Code table 4": self.value[4] & 0x08 == 0x08,
               "Code table 3": self.value[4] & 0x04 == 0x04,
               "Code table 2": self.value[4] & 0x02 == 0x02,
               "Code table 1": self.value[4] & 0x01 == 0x01
               }
        return self.strVal, msg
