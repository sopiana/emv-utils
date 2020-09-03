from DataObjects.GenericDO import GenericDO


class TerminalVerificationResults(GenericDO):
    def __init__(self, msg, tag="95", offset=0):
        GenericDO.__init__(self, msg, tag, offset)

    def parse(self, dataType='b'):
        msg = {"Offline data authentication was not performed": self.value[0] & 0x80 == 0x80,
               "SDA failed": self.value[0] & 0x40 == 0x40,
               "ICC data missing": self.value[0] & 0x20 == 0x20,
               "Card appears on terminal exception file": self.value[0] & 0x10 == 0x10,
               "DDA failed": self.value[0] & 0x08 == 0x08,
               "CDA failed": self.value[0] & 0x04 == 0x04,
               "RFU (B1b1-B1b2)": format(self.value[0] & 0x03, "02X"),
               "ICC and terminal have different application versions": self.value[1] & 0x80 == 0x80,
               "Expired application": self.value[1] & 0x40 == 0x40,
               "Application not yet effective": self.value[1] & 0x20 == 0x20,
               "Requested service not allowed for card product": self.value[1] & 0x10 == 0x10,
               "New card": self.value[1] & 0x08 == 0x08,
               "RFU (B2b1-B2b3)": format(self.value[1] & 0x07, "02X"),
               "Cardholder verification was not successful": self.value[2] & 0x80 == 0x80,
               "Unrecognised CVM": self.value[2] & 0x40 == 0x40,
               "PIN Try Limit exceeded": self.value[2] & 0x20 == 0x20,
               "PIN entry required and PIN pad not present or not working": self.value[2] & 0x10 == 0x10,
               "PIN entry required, PIN pad present, but PIN was not entered": self.value[2] & 0x08 == 0x08,
               "Online PIN entered": self.value[2] & 0x04 == 0x04,
               "RFU (B3b1-B3b2)": format(self.value[2] & 0x03, "02X"),
               "Transaction exceeds floor limit": self.value[3] & 0x80 == 0x80,
               "Lower consecutive offline limit exceeded": self.value[3] & 0x40 == 0x40,
               "Upper consecutive offline limit exceeded": self.value[3] & 0x20 == 0x20,
               "Transaction selected randomly for online processing": self.value[3] & 0x10 == 0x10,
               "Merchant forced transaction online": self.value[3] & 0x08 == 0x08,
               "RFU (B4b1-B4b3)": format(self.value[3] & 0x07, "02X"),
               "Default TDOL used": self.value[4] & 0x80 == 0x80,
               "Issuer authentication failed": self.value[4] & 0x40 == 0x40,
               "Script processing failed before final GENERATE AC": self.value[4] & 0x20 == 0x20,
               "Script processing failed after final GENERATE AC": self.value[4] & 0x10 == 0x10,
               "RFU (B5b1-B5b4)": format(self.value[4] & 0x0F, "02X"),
               }
        return self.strVal, msg
