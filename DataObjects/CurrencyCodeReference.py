from DataObjects.GenericDO import GenericDO
from Lib.ISO4217 import *


class CurrencyCodeReference(GenericDO):

    def __init__(self, msg, tag="9F3B", offset=0):
        GenericDO.__init__(self, msg, tag, offset)

    def parse(self, dataType='n'):
        currencyEtries = []
        for i in range(0, len(self.strVal), 4):
            currencyEtries.append(ISO4217.find_currency_code(self.strVal[i:i + 4]))
        return self.strVal, currencyEtries
