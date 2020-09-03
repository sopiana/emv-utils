from DataObjects.GenericDO import GenericDO
from Lib.ISO4217 import *


class CurrencyCode(GenericDO):

    def __init__(self, msg, tag="9F42", offset=0):
        GenericDO.__init__(self, msg, tag, offset)

    def parse(self, dataType='n'):
        return self.strVal, ISO4217.find_currency_code(self.strVal)
