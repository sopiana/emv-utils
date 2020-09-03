from DataObjects.GenericDO import GenericDO


class LogEntry(GenericDO):

    def __init__(self, msg, tag='9F4D', offset=0):
        GenericDO.__init__(self, msg, tag, offset)

    def parse(self, dataType='b'):
        return self.strVal, {"sfi": str(self.value[0]), "maximum record": str(self.value[1])}
