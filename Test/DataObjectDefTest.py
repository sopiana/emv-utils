import unittest

from DataObjects.DataObjectDefinitions import *


class MyTestCase(unittest.TestCase):
    def test_tag5F57(self):
        msg = "5F57 82 00 01 30 27 89"
        do = DataObjectDefinitions.find_do_by_tag('5F57')
        self.assertEqual(do["tag"], '5F57')
        obj = do["object"](msg)
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag9F01(self):
        msg = "9F01 06 31 32 33 34 35 36"
        do = DataObjectDefinitions.find_do_by_tag('9F01')
        self.assertEqual(do["tag"], '9F01')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag9F40(self):
        msg = "9F40 81 05 77 B5 41 12 01"
        do = DataObjectDefinitions.find_do_by_tag('9F40')
        self.assertEqual(do["tag"], '9F40')
        obj = do["object"](msg)
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag81(self):
        msg = "81 04 00 00 2B 51"
        do = DataObjectDefinitions.find_do_by_tag('81')
        self.assertEqual(do["tag"], '81')
        obj = do["object"](msg, '81')
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag9F04(self):
        msg = "9F04 81 04 00 00 2B 51"
        do = DataObjectDefinitions.find_do_by_tag('9F04')
        self.assertEqual(do["tag"], '9F04')
        obj = do["object"](msg, '9F04')
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag9F3A(self):
        msg = "9F3A 82 00 04 00 00 3C 42"
        do = DataObjectDefinitions.find_do_by_tag('9F3A')
        self.assertEqual(do["tag"], '9F3A')
        obj = do["object"](msg, '9F3A')
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag9F02(self):
        msg = "9F02 82 00 04 00 00 3C 42"
        do = DataObjectDefinitions.find_do_by_tag('9F02')
        self.assertEqual(do["tag"], '9F02')
        obj = do["object"](msg, '9F02')
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag9F03(self):
        msg = "9F03 04 00 00 00 12"
        do = DataObjectDefinitions.find_do_by_tag('9F03')
        self.assertEqual(do["tag"], '9F03')
        obj = do["object"](msg, '9F03')
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag9F42(self):
        msg = "9F42 81 02 00 08"
        do = DataObjectDefinitions.find_do_by_tag('9F42')
        self.assertEqual(do["tag"], '9F42')
        obj = do["object"](msg)
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse()))

    def test_tag9F44(self):
        msg = "9F44 01 02"
        do = DataObjectDefinitions.find_do_by_tag('9F44')
        self.assertEqual(do["tag"], '9F44')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag5F25(self):
        msg = "5F25 03 201125"
        do = DataObjectDefinitions.find_do_by_tag('5F25')
        self.assertEqual(do["tag"], '5F25')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag5F24(self):
        msg = "5F24 03 250131"
        do = DataObjectDefinitions.find_do_by_tag('5F24')
        self.assertEqual(do["tag"], '5F24')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag4F(self):
        msg = "4F 07 A0 00 00 60 01 00 01"
        do = DataObjectDefinitions.find_do_by_tag('4F')
        self.assertEqual(do["tag"], '4F')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag9F06(self):
        msg = "9F06 08 A0 00 00 60 01 00 01 01"
        do = DataObjectDefinitions.find_do_by_tag('9F06')
        self.assertEqual(do["tag"], '9F06')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag9F23(self):
        msg = "9F23 01 12"
        do = DataObjectDefinitions.find_do_by_tag('9F23')
        self.assertEqual(do["tag"], '9F23')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag9F37(self):
        msg = "9F37 04 12 34 56 78"
        do = DataObjectDefinitions.find_do_by_tag('9F37')
        self.assertEqual(do["tag"], '9F37')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag9C(self):
        msg = "9C 01 20"
        do = DataObjectDefinitions.find_do_by_tag('9C')
        self.assertEqual(do["tag"], '9C')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse()))

    def test_tag9F21(self):
        msg = "9F21 82 00 03 20 30 40"
        do = DataObjectDefinitions.find_do_by_tag('9F21')
        self.assertEqual(do["tag"], '9F21')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag9F41(self):
        msg = "9F41 04 53 20 9021"
        do = DataObjectDefinitions.find_do_by_tag('9F41')
        self.assertEqual(do["tag"], '9F41')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag9B(self):
        msg = "9B 02 53 00"
        do = DataObjectDefinitions.find_do_by_tag('9B')
        self.assertEqual(do["tag"], '9B')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse()))

    def test_tag9F3D(self):
        msg = "9F3D 81 01 02"
        do = DataObjectDefinitions.find_do_by_tag('9F3D')
        self.assertEqual(do["tag"], '9F3D')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag9F3C(self):
        msg = "9F3C 02 0360"
        do = DataObjectDefinitions.find_do_by_tag('9F3C')
        self.assertEqual(do["tag"], '9F3C')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse()))

    def test_tag9F26(self):
        msg = "9F26 08 036089A0 C78A766A"
        do = DataObjectDefinitions.find_do_by_tag('9F26')
        self.assertEqual(do["tag"], '9F26')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag9F05(self):
        msg = "9F05 81 10 036089A0 C78A766A036089A0 C78A766A"
        do = DataObjectDefinitions.find_do_by_tag('9F05')
        self.assertEqual(do["tag"], '9F05')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag94(self):
        msg = "94 10 08010300  18020300 18050600 20010302"
        do = DataObjectDefinitions.find_do_by_tag('94')
        self.assertEqual(do["tag"], '94')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse()))

    def test_tag50(self):
        msg = "50 0C 59 61 6e 67 20 53 6f 70 69 61 6e 61"
        do = DataObjectDefinitions.find_do_by_tag('50')
        self.assertEqual(do["tag"], '50')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag9F12(self):
        msg = "9F12 81 12 53 41 4d 50 4c 45 20 41 50 50 4c 49 43 41 54 49 4f 4e"
        do = DataObjectDefinitions.find_do_by_tag('9F12')
        self.assertEqual(do["tag"], '9F12')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag5F20(self):
        msg = "5F20 81 0C 53 4f 50 49 41 4e 41 5e 59 41 4e 47"
        do = DataObjectDefinitions.find_do_by_tag('5F20')
        self.assertEqual(do["tag"], '5F20')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag9F0B(self):
        msg = "9F0B 81 17 41 4c 46 41 54 49 48 5e 4d 55 48 41 4d 4d 41 44 5e 48 41 4d 5a 41 48"
        do = DataObjectDefinitions.find_do_by_tag('9F0B')
        self.assertEqual(do["tag"], '9F0B')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag5F50(self):
        msg = "5F50 28 68747470733a2f2f6170692e6769746875622e636f6d2f75736572732f6f63746f6361742f6f726773"
        do = DataObjectDefinitions.find_do_by_tag('5F50')
        self.assertEqual(do["tag"], '5F50')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag9F4E(self):
        msg = "9F4E 82 00 26 535441524255434b20534554494142554449204f4e45204a414b415254412053454c4154414e"
        do = DataObjectDefinitions.find_do_by_tag('9F4E')
        self.assertEqual(do["tag"], '9F4E')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag9F16(self):
        msg = "9F16 81 0D 4a2d434f204d45524348414e54"
        do = DataObjectDefinitions.find_do_by_tag('9F16')
        self.assertEqual(do["tag"], '9F16')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag9F3B(self):
        msg = "9F3B 02 4a2d434f204d45524348414e54"
        do = DataObjectDefinitions.find_do_by_tag('9F16')
        self.assertEqual(do["tag"], '9F16')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag5A(self):
        msg = "5A 08 12 34 56 78 90 12 3F FF"
        do = DataObjectDefinitions.find_do_by_tag('5A')
        self.assertEqual(do["tag"], '5A')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag9F20(self):
        msg = "9F20 0A 12 34 56 78 90 12 34 5F FF FF"
        do = DataObjectDefinitions.find_do_by_tag('9F20')
        self.assertEqual(do["tag"], '9F20')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag8A(self):
        msg = "8A 02 5933"
        do = DataObjectDefinitions.find_do_by_tag('8A')
        self.assertEqual(do["tag"], '8A')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag5F2D(self):
        msg = "5F2D 08 65 6e 68 72 6e 62 64 65"
        do = DataObjectDefinitions.find_do_by_tag('5F2D')
        self.assertEqual(do["tag"], '5F2D')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag9F1C(self):
        msg = "9F1C 08 4a 4b 54 53 45 4c 30 31"
        do = DataObjectDefinitions.find_do_by_tag('9F1C')
        self.assertEqual(do["tag"], '9F1C')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag9F1E(self):
        msg = "9F1E 81 08 49 4e 47 45 4e 49 43 4f"
        do = DataObjectDefinitions.find_do_by_tag('9F1E')
        self.assertEqual(do["tag"], '9F1E')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag82(self):
        msg = "82 02 7F00"
        do = DataObjectDefinitions.find_do_by_tag('82')
        self.assertEqual(do["tag"], '82')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse()))

    def test_tag5F34(self):
        msg = "5F34 01 03"
        do = DataObjectDefinitions.find_do_by_tag('5F34')
        self.assertEqual(do["tag"], '5F34')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag9F43(self):
        msg = "9F43 03 020100"
        do = DataObjectDefinitions.find_do_by_tag('9F43')
        self.assertEqual(do["tag"], '9F43')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag95(self):
        msg = "95 05 9C748D3A20"
        do = DataObjectDefinitions.find_do_by_tag('95')
        self.assertEqual(do["tag"], '95')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse()))

    def test_tag5F28(self):
        msg = "5F28 02 0270"
        do = DataObjectDefinitions.find_do_by_tag('5F28')
        self.assertEqual(do["tag"], '5F28')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag5F55(self):
        msg = "5F55 02 4944"
        do = DataObjectDefinitions.find_do_by_tag('5F55')
        self.assertEqual(do["tag"], '5F55')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag5F56(self):
        msg = "5F56 03 4d 43 4f"
        do = DataObjectDefinitions.find_do_by_tag('5F56')
        self.assertEqual(do["tag"], '5F56')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tag9F27(self):
        msg = "9F27 01 53"
        do = DataObjectDefinitions.find_do_by_tag('9F27')
        self.assertEqual(do["tag"], '9F27')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse()))

    def test_tag9F35(self):
        msg = "9F35 01 25"
        do = DataObjectDefinitions.find_do_by_tag('9F35')
        self.assertEqual(do["tag"], '9F35')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse()))

    def test_tag9F4D(self):
        msg = "9F4D 02 0B 05"
        do = DataObjectDefinitions.find_do_by_tag('9F4D')
        self.assertEqual(do["tag"], '9F4D')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse()))

    def test_tag87(self):
        msg = "87 01 83"
        do = DataObjectDefinitions.find_do_by_tag('87')
        self.assertEqual(do["tag"], '87')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse()))

    def test_tagTransactionReferenceCurrencyConversion(self):
        msg = "87 01 83 78 67 54 8A B5"
        do = DataObjectDefinitions.dictionary[134]
        self.assertEqual(do["name"], 'Transaction Reference Currency Conversion')
        obj = do["object"](msg, do["tag"], 2, 5)
        print(do["name"] + " (" + str(do["tag"]) + ") : " + str(obj.parse(do["format"])))

    def test_tag9F13(self):
        msg = "9F13 02 0230"
        do = DataObjectDefinitions.find_do_by_tag('9F13')
        self.assertEqual(do["tag"], '9F13')
        obj = do["object"](msg, do["tag"])
        print(do["name"] + " (" + do["tag"] + ") : " + str(obj.parse(do["format"])))

    def test_tagMaximumTargetPercentageTobeUsedForBiasedRandomSelection(self):
        msg = "01 02 03 04 05 06 07 08 09 0A"
        do = DataObjectDefinitions.dictionary[93]
        self.assertEqual(do["name"], 'Maximum Target Percentage to be used for Biased Random Selection')
        obj = do["object"](msg, do["tag"], 3, 5)
        print(do["name"] + " (" + str(do["tag"]) + ") : " + str(obj.parse(do["format"])))


if __name__ == '__main__':
    unittest.main()
