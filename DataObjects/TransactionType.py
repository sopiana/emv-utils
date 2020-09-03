from DataObjects.GenericDO import GenericDO
from Lib.ISO8583 import *


class TransactionType(GenericDO):

    def __init__(self, msg, tag='9C', offset=0):
        GenericDO.__init__(self, msg, tag, offset)

    def parse(self, dataType='n 3'):
        return self.strVal, ISO8583.find_transaction_code(self.strVal)
