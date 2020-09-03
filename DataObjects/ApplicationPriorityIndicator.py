from DataObjects.GenericDO import GenericDO


class ApplicationPriorityIndicator(GenericDO):

    def __init__(self, msg, tag="87", offset=0):
        GenericDO.__init__(self, msg, tag, offset)

    def parse(self, dataType='b'):
        msg = {"condition": self.value[0] & 0x80 != 0x80,
               "priority": str(self.value[0] & 0x0F)}
        return self.strVal, msg
