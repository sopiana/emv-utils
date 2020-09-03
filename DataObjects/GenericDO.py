import re

from Lib.HexUtils import *


class GenericDO(object):
    tag = None

    def __init__(self, msg, tag, offset=0, length=0):
        self.tag = tag
        msg = re.sub(r"\s+", "", msg, flags=re.ASCII).upper()

        if tag is not None:
            self.tag = re.sub(r"\s+", "", self.tag, flags=re.ASCII).upper()

            # if tag is present, remove the tag
            if msg.find(self.tag) != -1:
                msg = msg[msg.find(self.tag)+len(self.tag):]

            val = bytes.fromhex(msg)

            offset = 0
            if val[offset] & 0x80 == 0x80:
                lengthLen = val[offset] & 0x7F
                offset = offset + 1
                self.length = int.from_bytes(val[offset:offset + lengthLen], byteorder='big')
                offset = offset + lengthLen
            else:
                self.length = val[offset]
                offset = offset + 1
        else:
            self.length = length
            val = bytes.fromhex(msg)

        # TODO: add warnings if length is too big
        if (offset + self.length) * 2 > len(msg):
            print("length is too big " + str(self.length) + " : " + msg)

        self.value = val[offset: (offset + self.length)]
        self.strVal = msg[offset * 2: (offset + self.length) * 2]

    def parse(self, dataType='n'):
        if dataType is None or dataType.find('b') == 0:
            return self.strVal, self.strVal
        elif dataType.find('n') == 0:
            if is_all_bcd(self.value) is False:
                return self.strVal, self.strVal
            else:
                return self.strVal, self.value.decode('ASCII')
        elif dataType.find('ans') == 0:
            return self.strVal, self.value.decode('ASCII')
        elif dataType.find('cn') == 0:
            return self.strVal, self.strVal.rstrip('F')
        elif dataType.find('an') == 0:
            return self.strVal, self.value.decode('ASCII')
        return None
