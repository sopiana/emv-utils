from DataObjects.GenericDO import GenericDO


class TerminalType(GenericDO):

    def __init__(self, msg, tag='9F35', offset=0):
        GenericDO.__init__(self, msg, tag, offset)

    def parse(self, dataType='n 2'):
        msg = [{'1': "Controlled by Financial Institution", '2': "Controlled by Merchant",
                '3': "Controlled by Cardholder"}.get(self.strVal[0:1], "Unknown"),

               {'1': "Attended Online only", '2': "Attended Offline with online capability",
                '3': "Attended Offline only",
                '4': "Unattended Online only", '5': "Unattended Offline with online capability",
                '6': "Unattended Offline only"}.get(self.strVal[1:2], "Unknown")]
        return self.strVal, msg
