from DataObjects.GenericDO import GenericDO
from Lib.ISO3166 import *


class CountryCode(GenericDO):

    def __init__(self, msg, tag="5F28", offset=0):
        GenericDO.__init__(self, msg, tag, offset)

    def parse(self, dataType='n 3'):
        if dataType.find('n 3') != -1:
            return self.strVal, ISO3166.find_country_by_numeric_code(self.strVal)
        elif dataType.find('a 2') != -1:
            return self.strVal, ISO3166.find_country_by_alpha2(self.value.decode('ASCII'))
        elif dataType.find('a 3') != -1:
            return self.strVal, ISO3166.find_country_by_alpha3(self.value.decode('ASCII'))
