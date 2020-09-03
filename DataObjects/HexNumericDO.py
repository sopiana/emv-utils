from DataObjects.GenericDO import GenericDO


class HexNumericDO(GenericDO):

    def __init__(self, msg, tag, offset=0):
        GenericDO.__init__(self, msg, tag, offset)

    def parse(self, dataType='b'):
        return self.strVal, str(int(self.strVal, 16))
