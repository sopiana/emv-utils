from DataObjects.GenericDO import GenericDO


class CryptogramInformationData(GenericDO):

    def __init__(self, msg, tag="9F27", offset=0):
        GenericDO.__init__(self, msg, tag, offset)

    def parse(self, dataType='b'):
        msg = [{0: "AAC", 1: "TC", 2: "ARQC", 3: "RFU"}[(self.value[0] & 0xC0) >> 6]]
        if self.value[0] & 0x80 == 0x80:
            msg.append("Advice required")
        else:
            msg.append("No advice required")
        tempVal = self.value[0] & 0x07
        if tempVal == 0:
            msg.append("No information given")
        elif tempVal == 1:
            msg.append("Service not allowed")
        elif tempVal == 2:
            msg.append("PIN Try Limit exceeded")
        elif tempVal == 3:
            msg.append("Issuer authentication failed")
        else:
            msg.append("RFU")
        return self.strVal, msg
