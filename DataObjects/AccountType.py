from DataObjects.GenericDO import GenericDO


class AccountType(GenericDO):

    def __init__(self, msg, tag="5F57", offset=0):
        GenericDO.__init__(self, msg, tag, offset)

    def parse(self, dataType='n 2'):
        msg = {0x00: "Default - unspecified",
               0x10: "Savings",
               0x20: "Cheque/debit",
               0x30: "Credit"}.get(self.value[0], "RFU")
        return self.strVal, msg
