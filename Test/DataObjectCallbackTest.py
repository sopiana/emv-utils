import unittest

from DataObjects.DataObjectDefinitions import DataObjectDefinitions


class MyTestCase(unittest.TestCase):
    @staticmethod
    def test_read_dictionary():
        dictionary = DataObjectDefinitions.dictionary
        i = 0;
        for x in dictionary:
            try:
                x["object"]
            except KeyError:
                print(str(i)+" "+str(x))
                i = i + 1
        print("Total unimplemented DOs :" + str(i))


if __name__ == '__main__':
    unittest.main()
