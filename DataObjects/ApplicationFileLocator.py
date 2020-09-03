from DataObjects.GenericDO import GenericDO


class ApplicationFileLocator(GenericDO):

    def __init__(self, msg, tag="94", offset=0):
        GenericDO.__init__(self, msg, tag, offset)

    def parse(self, dataType='b'):
        if len(self.value) % 4 != 0:
            # TODO: add warnings if length is not multiple 4
            print("Warning: length is not multiple 4")
        aflEntries = []
        for i in range(0, len(self.value), 4):
            aflEntry = {
                "value": self.strVal[i * 2:(i + 4) * 2],
                "entry":
                    {
                        "sfi": str((self.value[i] & 0xF8) >> 3),
                        "firstRecord": self.value[i + 1],
                        "lastRecord": self.value[i + 2],
                        "numODARecord": self.value[i + 3]
                    }
            }
            aflEntries.append(aflEntry)
        return self.strVal, aflEntries
