import unittest

from DataObjects.DataObjectDefinitions import DataObjectDefinitions


class MyTestCase(unittest.TestCase):
    @staticmethod
    def test_read_dictionary():
        dictionary = DataObjectDefinitions.dictionary
        for x in dictionary:
            print(x["name"])


if __name__ == '__main__':
    unittest.main()
