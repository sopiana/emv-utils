from DataObjects import GenericDO
from DataObjects.AccountType import AccountType
from DataObjects.AdditionalTerminalCapabilities import AdditionalTerminalCapabilities
from DataObjects.ApplicationFileLocator import ApplicationFileLocator
from DataObjects.ApplicationInterchangeProfile import ApplicationInterchangeProfile
from DataObjects.ApplicationPriorityIndicator import ApplicationPriorityIndicator
from DataObjects.CountryCode import CountryCode
from DataObjects.CryptogramInformationData import CryptogramInformationData
from DataObjects.CurrencyCode import CurrencyCode
from DataObjects.CurrencyCodeReference import CurrencyCodeReference
from DataObjects.GenericDO import GenericDO
from DataObjects.HexNumericDO import HexNumericDO
from DataObjects.LogEntry import LogEntry
from DataObjects.TerminalType import TerminalType
from DataObjects.TerminalVerificationResults import TerminalVerificationResults
from DataObjects.TransactionStatusInformation import TransactionStatusInformation
from DataObjects.TransactionType import TransactionType


class DataObjectDefinitions:
    def __init__(self):
        pass
    TEST = ("Account Type", "Ind")
    dictionary = [
        {
            "name": "Account Type",
            "description": "Indicates the type of account selected on the terminal, coded as specified in Annex G",
            "source": "Terminal",
            "format": "n 2",
            "template": None,
            "tag": "5F57",
            "length": "1",
            "object": AccountType
        },
        {
            "name": "Acquirer Identifier",
            "description": "Uniquely identifies the acquirer within each payment system",
            "source": "Terminal",
            "format": "n 6-11",
            "template": None,
            "tag": "9F01",
            "length": "6",
            "object": GenericDO
        },
        {
            "name": "Additional Terminal Capabilities",
            "description": "Indicates the data input and output capabilities of the terminal",
            "source": "Terminal",
            "format": "b",
            "template": None,
            "tag": "9F40",
            "length": "5",
            "object": AdditionalTerminalCapabilities
        },
        {
            "name": "Amount, Authorised (Binary)",
            "description": "Authorised amount of the transaction (excluding adjustments)",
            "source": "Terminal",
            "format": "b",
            "template": None,
            "tag": "81",
            "length": "4",
            "object": HexNumericDO
        },
        {
            "name": "Amount, Authorised (Numeric)",
            "description": "Authorised amount of the transaction (excluding adjustments)",
            "source": "Terminal",
            "format": "n 12",
            "template": None,
            "tag": "9F02",
            "length": "6",
            "object": GenericDO
        },
        {
            "name": "Amount, Other (Binary)",
            "description": "Secondary amount associated with the transaction representing a cashback amount",
            "source": "Terminal",
            "format": "b",
            "template": None,
            "tag": "9F04",
            "length": "4",
            "object": HexNumericDO
        },
        {
            "name": "Amount, Other (Numeric)",
            "description": "Secondary amount associated with the transaction representing a cashback amount",
            "source": "Terminal",
            "format": "n 12",
            "template": None,
            "tag": "9F03",
            "length": "6",
            "object": GenericDO
        },
        {
            "name": "Amount, Reference Currency",
            "description": "Authorised amount expressed in the reference currency",
            "source": "Terminal",
            "format": "b",
            "template": None,
            "tag": "9F3A",
            "length": "4",
            "object": HexNumericDO
        },
        {
            "name": "Application Cryptogram",
            "description": "Cryptogram returned by the ICC in response of the GENERATE AC command",
            "source": "ICC",
            "format": "b",
            "template": "77 or 80",
            "tag": "9F26",
            "length": "8",
            "object": GenericDO
        },
        {
            "name": "Application Currency Code",
            "description": "Indicates the currency in which the account is managed according to ISO 4217",
            "source": "ICC",
            "format": "n 3",
            "template": "70 or 77",
            "tag": "9F42",
            "length": "2",
            "object": CurrencyCode
        },
        {
            "name": "Application Currency Exponent",
            "description": "Indicates the implied position of the decimal point from the right of the amount "
                           "represented according to ISO 4217",
            "source": "ICC",
            "format": "n 1",
            "template": "70 or 77",
            "tag": "9F44",
            "length": "1",
            "object": GenericDO
        },
        {
            "name": "Application Discretionary Data",
            "description": "Issuer or payment system specified data relating to the application",
            "source": "ICC",
            "format": "b",
            "template": "70 or 77",
            "tag": "9F05",
            "length": "1-32",
            "object": GenericDO
        },
        {
            "name": "Application Effective Date",
            "description": "Date from which the application may be used ",
            "source": "ICC",
            "format": "n 6 YYMMDD",
            "template": "70 or 77",
            "tag": "5F25",
            "length": "3",
            "object": GenericDO
        },
        {
            "name": "Application Expiration Date",
            "description": "Date after which application expires ",
            "source": "ICC",
            "format": "n 6 YYMMDD",
            "template": "70 or 77",
            "tag": "5F24",
            "length": "3",
            "object": GenericDO
        },
        {
            "name": "Application File Locator (AFL)",
            "description": "Indicates the location (SFI, range of records) of the AEFs related to a given application",
            "source": "ICC",
            "format": "var.",
            "template": "77 or 80",
            "tag": "94",
            "length": "var. up to 252",
            "object": ApplicationFileLocator
        },
        {
            "name": "Application Dedicated File (ADF) Name",
            "description": "Identifies the application as described in ISO/IEC 7816-5",
            "source": "ICC",
            "format": "b",
            "template": "61",
            "tag": "4F",
            "length": "5-16",
            "object": GenericDO
        },
        {
            "name": "Application Identifier (AID) – terminal",
            "description": "Identifies the application as described in ISO/IEC 7816-5",
            "source": "Terminal",
            "format": "b",
            "template": None,
            "tag": "9F06",
            "length": "5-16",
            "object": GenericDO
        },
        {
            "name": "Application Interchange Profile",
            "description": "Indicates the capabilities of the card to support specific functions in the application",
            "source": "ICC",
            "format": "b",
            "template": "77 or 80",
            "tag": "82",
            "length": "2",
            "object": ApplicationInterchangeProfile
        },
        {
            "name": "Application Label",
            "description": "Mnemonic associated with the AID according to ISO/IEC 7816-5",
            "source": "ICC",
            "format": "ans with the special character limited to space",
            "template": "61 or A5",
            "tag": "50",
            "length": "1-16",
            "object": GenericDO
        },
        {
            "name": "Application Preferred Name",
            "description": "Preferred mnemonic associated with the AID",
            "source": "ICC",
            "format": "ans (see section 4.3)",
            "template": "61 or A5",
            "tag": "9F12",
            "length": "1-16",
            "object": GenericDO
        },
        {
            "name": "Application Primary Account Number (PAN)",
            "description": "Valid cardholder account number ",
            "source": "ICC",
            "format": "cn var. up to 19",
            "template": "70 or 77",
            "tag": "5A",
            "length": "var. up to 10",
            "object": GenericDO
        },
        {
            "name": "Application Primary Account Number (PAN) Sequence Number",
            "description": "Identifies and differentiates cards with the same PAN",
            "source": "ICC",
            "format": "n 2",
            "template": "70 or 77",
            "tag": "5F34",
            "length": "1",
            "object": GenericDO
        },
        {
            "name": "Application Priority Indicator",
            "description": "Indicates the priority of a given application or group of applications in a directory",
            "source": "ICC",
            "format": "b",
            "template": "61 or A5",
            "tag": "87",
            "length": "1",
            "object": ApplicationPriorityIndicator
        },
        {
            "name": "Application Reference Currency",
            "description": "1-4 currency codes used between the terminal and the ICC when the Transaction Currency "
                           "Code is different from the Application Currency Code; each code is 3 digits according to "
                           "ISO 4217",
            "source": "ICC",
            "format": "n 3",
            "template": "70 or 77",
            "tag": "9F3B",
            "length": "2-8",
            "object": CurrencyCodeReference
        },
        {
            "name": "Application Reference Currency Exponent",
            "description": "Indicates the implied position of the decimal point from the right of the amount, "
                           "for each of the 1-4 reference currencies represented according to ISO 4217",
            "source": "ICC",
            "format": "n 1",
            "template": "70 or 77",
            "tag": "9F43",
            "length": "1-4",
            "object": GenericDO
        },
        {
            "name": "Application Selection Indicator",
            "description": "For an application in the ICC to be supported by an application in the terminal, "
                           "the Application Selection Indicator indicates whether the associated AID in the terminal "
                           "must match the AID in the card exactly, including the length of the AID, or only up to "
                           "the length of the AID in the terminal <br/>"
                           "There is only one Application Selection Indicator per AID supported by the terminal",
            "source": "Terminal",
            "format": "At the discretion of the terminal. The data is not sent across the interface",
            "template": None,
            "tag": None,
            "length": "See format"
        },
        {
            "name": "Application Template",
            "description": "Contains one or more data objects relevant to an application directory entry according to "
                           "ISO/IEC 7816-5",
            "source": "ICC",
            "format": "b",
            "template": "70",
            "tag": "61",
            "length": "var. up to 252"
        },
        {
            "name": "Application Transaction Counter (ATC)",
            "description": "Counter maintained by the application in the ICC (incrementing the ATC is managed by the "
                           "ICC)",
            "source": "ICC",
            "format": "b",
            "template": "77 or 80",
            "tag": "9F36",
            "length": "2",
            "object": GenericDO
        },
        {
            "name": "Application Usage Control",
            "description": "Indicates issuer’s specified restrictions on the geographic usage and services allowed "
                           "for the application",
            "source": "ICC",
            "format": "b",
            "template": "70 or 77",
            "tag": "9F07",
            "length": "2"
        },
        {
            "name": "Application Version Number",
            "description": "Version number assigned by the payment system for the application",
            "source": "ICC",
            "format": "b",
            "template": "70 or 77",
            "tag": "9F08",
            "length": "2",
            "object": GenericDO
        },
        {
            "name": "Application Version Number - Terminal",
            "description": "Version number assigned by the payment system for the application",
            "source": "Terminal",
            "format": "b",
            "template": None,
            "tag": "9F09",
            "length": "2",
            "object": GenericDO
        },
        {
            "name": "Authorisation Code",
            "description": "Value generated by the authorisation authority for an approved transaction",
            "source": "Issuer",
            "format": "As defined by the Payment Systems",
            "template": None,
            "tag": "89",
            "length": "6",
            "object": GenericDO
        },
        {
            "name": "Authorisation Response Code",
            "description": "Code that defines the disposition of a message",
            "source": "Issuer/Terminal",
            "format": "an 2",
            "template": None,
            "tag": "8A",
            "length": "2",
            "object": GenericDO
        },
        {
            "name": "Authorisation Response Cryptogram (ARPC)",
            "description": "Cryptogram generated by the issuer and used by the card to verify that the response came "
                           "from the issuer.",
            "source": "Issuer",
            "format": "b",
            "template": None,
            "tag": None,
            "length": "4 or 8",
            "object": GenericDO
        },
        {
            "name": "Bank Identifier Code (BIC)",
            "description": "Uniquely identifies a bank as defined in ISO 9362.",
            "source": "ICC",
            "format": "var.",
            "template": "BF0C or 73",
            "tag": "5F54",
            "length": "8 or 11"
        },
        {
            "name": "Card Risk Management Data Object List 1 (CDOL1)",
            "description": "List of data objects (tag and length) to be passed to the ICC in the first GENERATE AC "
                           "command",
            "source": "ICC",
            "format": "b",
            "template": "70 or 77",
            "tag": "8C",
            "length": "var. up to 252"
        },
        {
            "name": "Card Risk Management Data Object List 2 (CDOL2)",
            "description": "List of data objects (tag and length) to be passed to the ICC in the second GENERATE AC "
                           "command",
            "source": "ICC",
            "format": "b",
            "template": "70 or 77",
            "tag": "8D",
            "length": "var. up to 252"
        },
        {
            "name": "Card Status Update (CSU)",
            "description": "Contains data sent to the ICC to indicate whether the issuer approves or declines the "
                           "transaction, and to initiate actions specified by the issuer. Transmitted to the card in "
                           "Issuer Authentication Data.",
            "source": "Issuer",
            "format": "b",
            "template": None,
            "tag": None,
            "length": "4"
        },
        {
            "name": "Cardholder Name",
            "description": "Indicates cardholder name according to ISO 7813",
            "source": "ICC",
            "format": "ans 2-26",
            "template": "70 or 77",
            "tag": "5F20",
            "length": "2-26",
            "object": GenericDO
        },
        {
            "name": "Cardholder Name Extended",
            "description": "Indicates the whole cardholder name when greater than 26 characters using the same coding "
                           "convention as in ISO 7813",
            "source": "ICC",
            "format": "ans 27-45",
            "template": "70 or 77",
            "tag": "9F0B",
            "length": "27-45",
            "object": GenericDO
        },
        {
            "name": "Cardholder Verification Method (CVM) List",
            "description": "Identifies a method of verification of the cardholder supported by the application",
            "source": "ICC",
            "format": "b",
            "template": "70 or 77",
            "tag": "8E",
            "length": "10-252"
        },
        {
            "name": "Cardholder Verification Method (CVM) Results",
            "description": "Indicates the results of the last CVM performed",
            "source": "Terminal",
            "format": "b",
            "template": None,
            "tag": "9F34",
            "length": "3"
        },
        {
            "name": "Certification Authority Public Key Check Sum",
            "description": "A check value calculated on the concatenation of all parts of the Certification Authority "
                           "Public Key (RID, Certification Authority Public Key Index, Certification Authority Public "
                           "Key Modulus, Certification Authority Public Key Exponent) using SHA-1",
            "source": "Terminal",
            "format": "b",
            "template": None,
            "tag": None,
            "length": "20",
            "object": GenericDO
        },
        {
            "name": "Certification Authority Public Key Exponent",
            "description": "Value of the exponent part of the Certification Authority Public Key",
            "source": "Terminal",
            "format": "b",
            "template": None,
            "tag": None,
            "length": "1 or 3",
            "object": GenericDO
        },
        {
            "name": "Certification Authority Public Key Index",
            "description": "Identifies the certification authority’s public key in conjunction with the RID",
            "source": "ICC",
            "format": "b",
            "template": "70 or 77",
            "tag": "8F",
            "length": "1",
            "object": GenericDO
        },
        {
            "name": "Certification Authority Public Key Index",
            "description": "Identifies the certification authority’s public key in conjunction with the RID",
            "source": "Terminal",
            "format": "b",
            "template": None,
            "tag": "9F22",
            "length": "1",
            "object": GenericDO
        },
        {
            "name": "Certification Authority Public Key Modulus",
            "description": "Value of the modulus part of the Certification Authority Public Key",
            "source": "Terminal",
            "format": "b",
            "template": None,
            "tag": None,
            "length": "NCA (up to 248)",
            "object": GenericDO
        },
        {
            "name": "Command Template",
            "description": "Identifies the data field of a command message",
            "source": "Terminal",
            "format": "b",
            "template": None,
            "tag": "83",
            "length": "var."
        },
        {
            "name": "Cryptogram Information Data",
            "description": "Indicates the type of cryptogram and the actions to be performed by the terminal",
            "source": "ICC",
            "format": "b",
            "template": "77 or 80",
            "tag": "9F27",
            "length": "1",
            "object": CryptogramInformationData
        },
        {
            "name": "Data Authentication Code",
            "description": "An issuer assigned value that is retained by the terminal during the verification process "
                           "of the Signed Static Application Data",
            "source": "ICC",
            "format": "b",
            "template": None,
            "tag": "9F45",
            "length": "2",
            "object": GenericDO
        },
        {
            "name": "Dedicated File (DF) Name",
            "description": "Identifies the name of the DF as described in ISO/IEC 7816-4",
            "source": "ICC",
            "format": "b",
            "template": "6F",
            "tag": "84",
            "length": "5-16",
            "object": GenericDO
        },
        {
            "name": "Default Dynamic Data Authentication Data Object List (DDOL)",
            "description": "DDOL to be used for constructing the INTERNAL AUTHENTICATE command if the DDOL in the "
                           "card is not present",
            "source": "Terminal",
            "format": "b",
            "template": None,
            "tag": None,
            "length": "var."
        },
        {
            "name": "Default Transaction Certificate Data Object List (TDOL)",
            "description": "TDOL to be used for generating the TC Hash Value if the TDOL in the card is not present",
            "source": "Terminal",
            "format": "b",
            "template": None,
            "tag": None,
            "length": "var."
        },
        {
            "name": "Directory Definition File (DDF) Name",
            "description": "Identifies the name of a DF associated with a directory",
            "source": "ICC",
            "format": "b",
            "template": "61",
            "tag": "9D",
            "length": "5-16",
            "object": GenericDO
        },
        {
            "name": "Directory Discretionary Template",
            "description": "Issuer discretionary part of the directory according to ISO/IEC 7816-5",
            "source": "ICC",
            "format": "var.",
            "template": "61",
            "tag": "73",
            "length": "var. up to 252"
        },
        {
            "name": "Dynamic Data Authentication Data Object List (DDOL)",
            "description": "List of data objects (tag and length) to be passed to the ICC in the INTERNAL "
                           "AUTHENTICATE command",
            "source": "ICC",
            "format": "b",
            "template": "70 or 77",
            "tag": "9F49",
            "length": "up to 252"
        },
        {
            "name": "Enciphered Personal Identification Number (PIN) Data",
            "description": "Transaction PIN enciphered at the PIN pad for online verification or for offline "
                           "verification if the PIN pad and IFD are not a single integrated device",
            "source": "Terminal",
            "format": "b",
            "template": None,
            "tag": None,
            "length": "8",
            "object": GenericDO
        },
        {
            "name": "File Control Information (FCI) Issuer Discretionary Data",
            "description": "Issuer discretionary part of the FCI ",
            "source": "ICC",
            "format": "var.",
            "template": "A5",
            "tag": "BF0C",
            "length": "var. up to 222"
        },
        {
            "name": "File Control Information (FCI) Proprietary Template",
            "description": "Identifies the data object proprietary to this specification in the FCI template "
                           "according to ISO/IEC 7816-4",
            "source": "ICC",
            "format": "var.",
            "template": "6F",
            "tag": "A5",
            "length": "var."
        },
        {
            "name": "File Control Information (FCI) Template",
            "description": "Identifies the FCI template according to ISO/IEC 7816-4",
            "source": "ICC",
            "format": "var.",
            "template": None,
            "tag": "6F",
            "length": "var. up to 252"
        },
        {
            "name": "ICC Dynamic Number",
            "description": "Time-variant number generated by the ICC, to be captured by the terminal",
            "source": "ICC",
            "format": "b",
            "template": None,
            "tag": "9F4C",
            "length": "2-8",
            "object": GenericDO
        },
        {
            "name": "Integrated Circuit Card (ICC) PIN Encipherment Public Key Certificate",
            "description": "ICC PIN Encipherment Public Key certified by the issuer",
            "source": "ICC",
            "format": "b",
            "template": "70 or 77",
            "tag": "9F2D",
            "length": "NI",
            "object": GenericDO
        },
        {
            "name": "Integrated Circuit Card (ICC) PIN Encipherment Public Key Exponent",
            "description": "ICC PIN Encipherment Public Key Exponent used for PIN encipherment",
            "source": "ICC",
            "format": "b",
            "template": "70 or 77",
            "tag": "9F2E",
            "length": "1 or 3",
            "object": GenericDO
        },
        {
            "name": "Integrated Circuit Card (ICC) PIN Encipherment Public Key Remainder",
            "description": "Remaining digits of the ICC PIN Encipherment Public Key Modulus",
            "source": "ICC",
            "format": "b",
            "template": "70 or 77",
            "tag": "9F2F",
            "length": "NPE − NI + 42",
            "object": GenericDO
        },
        {
            "name": "Integrated Circuit Card (ICC) Public Key Certificate",
            "description": "ICC Public Key certified by the issuer",
            "source": "ICC",
            "format": "b",
            "template": "70 or 77",
            "tag": "9F46",
            "length": "NI",
            "object": GenericDO
        },
        {
            "name": "Integrated Circuit Card (ICC) Public Key Exponent",
            "description": "ICC Public Key Exponent used for the verification of the Signed Dynamic Application Data",
            "source": "ICC",
            "format": "b",
            "template": "70 or 77",
            "tag": "9F47",
            "length": "1 to 3",
            "object": GenericDO
        },
        {
            "name": "Integrated Circuit Card (ICC) Public Key Remainder",
            "description": "Remaining digits of the ICC Public Key Modulus",
            "source": "ICC",
            "format": "b",
            "template": "70 or 77",
            "tag": "9F48",
            "length": "NIC − NI + 42",
            "object": GenericDO
        },
        {
            "name": "Interface Device (IFD) Serial Number",
            "description": "Unique and permanent serial number assigned to the IFD by the manufacture",
            "source": "Terminal",
            "format": "an 8",
            "template": None,
            "tag": "9F1E",
            "length": "8",
            "object": GenericDO
        },
        {
            "name": "International Bank Account Number (IBAN)",
            "description": "Uniquely identifies the account of a customer at a financial institution as defined in "
                           "ISO 13616.",
            "source": "ICC",
            "format": "var.",
            "template": "BF0C or 73",
            "tag": "5F53",
            "length": "Var. up to 34"
        },
        {
            "name": "Issuer Action Code - Default",
            "description": "Specifies the issuer’s conditions that cause a transaction to be rejected if it might "
                           "have been approved online, but the terminal is unable to process the transaction online",
            "source": "ICC",
            "format": "b",
            "template": "70 or 77",
            "tag": "9F0D",
            "length": "5",
            "object": TerminalVerificationResults
        },
        {
            "name": "Issuer Action Code - Denial",
            "description": "Specifies the issuer’s conditions that cause the denial of a transaction without attempt "
                           "to go online",
            "source": "ICC",
            "format": "b",
            "template": "70 or 77",
            "tag": "9F0E",
            "length": "5",
            "object": TerminalVerificationResults
        },
        {
            "name": "Issuer Action Code - Online",
            "description": "Specifies the issuer’s conditions that cause a transaction to be transmitted online",
            "source": "ICC",
            "format": "b",
            "template": "70 or 77",
            "tag": "9F0F",
            "length": "5",
            "object": TerminalVerificationResults
        },
        {
            "name": "Issuer Application Data",
            "description": "Contains proprietary application data for transmission to the issuer in an online "
                           "transaction.<br/>Note: For CCD-compliant applications, Annex C, section C7 defines the "
                           "specific coding of the Issuer Application Data (IAD). To avoid potential conflicts with "
                           "CCD-compliant applications, it is strongly recommended that the IAD data element in an "
                           "application that is not CCD-compliant should not use the coding for a CCD-compliant "
                           "application",
            "source": "ICC",
            "format": "b",
            "template": "77 or 80",
            "tag": "9F10",
            "length": "var. up to 32"
        },
        {
            "name": "Issuer Authentication Data",
            "description": "Data sent to the ICC for online issuer authentication",
            "source": "Issuer",
            "format": "b",
            "template": None,
            "tag": "91",
            "length": "8-16"
        },
        {
            "name": "Issuer Code Table Index",
            "description": "Indicates the code table according to ISO/IEC 8859 for displaying the Application "
                           "Preferred Name",
            "source": "ICC",
            "format": "n 2",
            "template": "A5",
            "tag": "9F11",
            "length": "1"
        },
        {
            "name": "Issuer Country Code",
            "description": "Indicates the country of the issuer according to ISO 3166",
            "source": "ICC",
            "format": "n 3",
            "template": "70 or 77",
            "tag": "5F28",
            "length": "2",
            "object": CountryCode
        },
        {
            "name": "Issuer Country Code (alpha2 format)",
            "description": "Indicates the country of the issuer as defined in ISO 3166 (using a 2 character "
                           "alphabetic code)",
            "source": "ICC",
            "format": "a 2",
            "template": "BF0C or 73",
            "tag": "5F55",
            "length": "2",
            "object": CountryCode
        },
        {
            "name": "Issuer Country Code (alpha3 format)",
            "description": "Indicates the country of the issuer as defined in ISO 3166 (using a 3 character "
                           "alphabetic code)",
            "source": "ICC",
            "format": "a 3",
            "template": "BF0C or 73",
            "tag": "5F56",
            "length": "3",
            "object": CountryCode
        },
        {
            "name": "Issuer Identification Number (IIN)",
            "description": "The number that identifies the major industry and the card issuer and that forms the "
                           "first part of the Primary Account Number (PAN)",
            "source": "ICC",
            "format": "n 6",
            "template": "BF0C or 73",
            "tag": "42",
            "length": "3"
        },
        {
            "name": "Issuer Public Key Certificate",
            "description": "Issuer public key certified by a certification authority",
            "source": "ICC",
            "format": "b",
            "template": "70 or 77",
            "tag": "90",
            "length": "NCA",
            "object": GenericDO
        },
        {
            "name": "Issuer Public Key Exponent",
            "description": "Issuer public key exponent used for the verification of the Signed Static Application "
                           "Data and the ICC Public Key Certificate",
            "source": "ICC",
            "format": "b",
            "template": "70 or 77",
            "tag": "9F32",
            "length": "1 to 3",
            "object": GenericDO
        },
        {
            "name": "Issuer Public Key Remainder",
            "description": "Remaining digits of the Issuer Public Key Modulus",
            "source": "ICC",
            "format": "b",
            "template": "70 or 77",
            "tag": "92",
            "length": "NI − NCA + 36",
            "object": GenericDO
        },
        {
            "name": "Issuer Script Command",
            "description": "Contains a command for transmission to the ICC",
            "source": "Issuer",
            "format": "b",
            "template": "71 or 72",
            "tag": "86",
            "length": "var. up to 261",
            "object": GenericDO
        },
        {
            "name": "Issuer Script Identifier",
            "description": "Identification of the Issuer Script ",
            "source": "Issuer",
            "format": "b",
            "template": "71 or 72",
            "tag": "9F18",
            "length": "4",
            "object": GenericDO
        },
        {
            "name": "Issuer Script Results",
            "description": "Indicates the result of the terminal script processing",
            "source": "Terminal",
            "format": "b",
            "template": None,
            "tag": None,
            "length": "var."
        },
        {
            "name": "Issuer Script Template 1",
            "description": "Contains proprietary issuer data for transmission to the ICC before the second GENERATE "
                           "AC command",
            "source": "Issuer",
            "format": "b",
            "template": None,
            "tag": "71",
            "length": "var."
        },
        {
            "name": "Issuer Script Template 2",
            "description": "Contains proprietary issuer data for transmission to the ICC after the second GENERATE AC "
                           "command",
            "source": "Issuer",
            "format": "b",
            "template": None,
            "tag": "72",
            "length": "var."
        },
        {
            "name": "Issuer URL",
            "description": "The URL provides the location of the Issuer’s  Library Server on the Internet.",
            "source": "ICC",
            "format": "ans",
            "template": "BF0C or 73",
            "tag": "5F50",
            "length": "var.",
            "object": GenericDO
        },
        {
            "name": "Language Preference",
            "description": "1-4 languages stored in order of preference, each represented by 2 alphabetical "
                           "characters according to ISO 639 <br/>Note: EMVCo strongly recommends that cards be "
                           "personalised with data element '5F2D' coded in lowercase, but that terminals accept the "
                           "data element whether it is coded in upper or lower case.",
            "source": "ICC",
            "format": "an 2",
            "template": "A5",
            "tag": "5F2D",
            "length": "2-8",
            "object": GenericDO
        },
        {
            "name": "Last Online Application Transaction Counter (ATC)",
            "description": "Register ATC value of the last transaction that went online",
            "source": "ICC",
            "format": "b",
            "template": None,
            "tag": "9F13",
            "length": "2",
            "object": GenericDO
        },
        {
            "name": "Log Entry",
            "description": "Provides the SFI of the Transaction Log file and its number of records",
            "source": "ICC",
            "format": "b",
            "template": "BF0C or 73",
            "tag": "9F4D",
            "length": "2",
            "object": LogEntry
        },
        {
            "name": "Log Format",
            "description": "List (in tag and length format) of data objects representing the logged data elements "
                           "that are passed to the terminal when a transaction log record is read",
            "source": "ICC",
            "format": "b",
            "template": None,
            "tag": "9F4F",
            "length": "var."
        },
        {
            "name": "Lower Consecutive Offline Limit",
            "description": "Issuer-specified preference for the maximum number of consecutive offline transactions "
                           "for this ICC application allowed in a terminal with online capability",
            "source": "ICC",
            "format": "b",
            "template": "70 or 77",
            "tag": "9F14",
            "length": "1",
            "object": GenericDO
        },
        {
            "name": "Maximum Target Percentage to be used for Biased Random Selection",
            "description": "Value used in terminal risk management for random transaction selection",
            "source": "Terminal",
            "format": None,
            "template": None,
            "tag": None,
            "length": None,
            "object": GenericDO
        },
        {
            "name": "Merchant Category Code",
            "description": "Classifies the type of business being done by the merchant, represented according to ISO "
                           "8583:1993 for Card Acceptor Business Code",
            "source": "Terminal",
            "format": "n 4",
            "template": None,
            "tag": "9F15",
            "length": "2"
        },
        {
            "name": "Merchant Identifier",
            "description": "When concatenated with the Acquirer Identifier, uniquely identifies a given merchant",
            "source": "Terminal",
            "format": "ans 15",
            "template": None,
            "tag": "9F16",
            "length": "15",
            "object": GenericDO
        },
        {
            "name": "Merchant Name and Location",
            "description": "Indicates the name and location of the merchant",
            "source": "Terminal",
            "format": "ans",
            "template": None,
            "tag": "9F4E",
            "length": "var.",
            "object": GenericDO
        },
        {
            "name": "Message Type",
            "description": "Indicates whether the batch data capture record is a financial record or advice",
            "source": "Terminal",
            "format": "n 2",
            "template": None,
            "tag": None,
            "length": "1"
        },
        {
            "name": "Personal Identification Number (PIN)",
            "description": "Pad Secret Key Secret key of a symmetric algorithm used by the PIN pad to encipher the "
                           "PIN and by the card reader to decipher the PIN if the PIN pad and card reader are not "
                           "integrated",
            "source": "Terminal",
            "format": None,
            "template": None,
            "tag": None,
            "length": None
        },
        {
            "name": "Personal Identification Number (PIN) Try Counter",
            "description": "Number of PIN tries remaining",
            "source": "ICC",
            "format": "b",
            "template": None,
            "tag": "9F17",
            "length": "1"
        },
        {
            "name": "Point-of-Service (POS) Entry Mode",
            "description": "Indicates the method by which the PAN was entered, according to the first two digits of "
                           "the ISO 8583:1987 POS Entry Mode",
            "source": "Terminal",
            "format": "n 2",
            "template": None,
            "tag": "9F39",
            "length": "1"
        },
        {
            "name": "Processing Options Data Object List (PDOL)",
            "description": "Contains a list of terminal resident data objects (tags and lengths) needed by the ICC in "
                           "processing the GET PROCESSING OPTIONS command",
            "source": "ICC",
            "format": "b",
            "template": "A5",
            "tag": "9F38",
            "length": "var."
        },
        {
            "name": "Proprietary Authentication Data",
            "description": "Contains issuer data for transmission to the card in the Issuer Authentication Data of an "
                           "online transaction.",
            "source": "Issuer",
            "format": "b",
            "template": None,
            "tag": None,
            "length": "var. up to 8",
            "object": GenericDO
        },
        {
            "name": "READ RECORD Response Message Template",
            "description": "Contains the contents of the record read. (Mandatory for SFIs 1-10. Response messages for "
                           "SFIs 11-30 are outside the scope of EMV, but may use template '70')",
            "source": "ICC",
            "format": "var.",
            "template": None,
            "tag": "70",
            "length": "var. up to 252"
        },
        {
            "name": "Response Message Template Format 1",
            "description": "Contains the data objects (without tags and lengths) returned by the ICC in response to a "
                           "command",
            "source": "ICC",
            "format": "var.",
            "template": None,
            "tag": "80",
            "length": "var."
        },
        {
            "name": "Response Message Template Format 2",
            "description": "Contains the data objects (with tags and lengths) returned by the ICC in response to a "
                           "command",
            "source": "ICC",
            "format": "var.",
            "template": None,
            "tag": "77",
            "length": "var."
        },
        {
            "name": "Service Code",
            "description": "Service code as defined in ISO/IEC 7813 for track 1 and track 2",
            "source": "ICC",
            "format": "n 3",
            "template": "70 or 77",
            "tag": "5F30",
            "length": "2",
            "object": GenericDO
        },
        {
            "name": "Short File Identifier (SFI)",
            "description": "Identifies the AEF referenced in commands related to a given ADF or DDF. It is a binary "
                           "data object having a value in the range 1 to 30 and with the three high order bits set to"
                           " zero.",
            "source": "ICC",
            "format": "b",
            "template": "A5",
            "tag": "88",
            "length": "1",
            "object": GenericDO
        },
        {
            "name": "Signed Dynamic Application Data",
            "description": "Digital signature on critical application parameters for DDA or CDA",
            "source": "ICC",
            "format": "b",
            "template": "77 or 80",
            "tag": "9F4B",
            "length": "NIC",
            "object": GenericDO
        },
        {
            "name": "Signed Static Application Data",
            "description": "Digital signature on critical application parameters for SDA",
            "source": "ICC",
            "format": "b",
            "template": "70 or 77",
            "tag": "93",
            "length": "NI",
            "object": GenericDO
        },
        {
            "name": "Static Data Authentication Tag List",
            "description": "List of tags of primitive data objects defined in this specification whose value fields "
                           "are to be included in the Signed Static or Dynamic Application Data",
            "source": "ICC",
            "format": None,
            "template": "70 or 77",
            "tag": "9F4A",
            "length": "var."
        },
        {
            "name": "Target Percentage to be Used for Random Selection",
            "description": "Value used in terminal risk management for random transaction selection",
            "source": "Terminal",
            "format": None,
            "template": None,
            "tag": None,
            "length": None,
            "object": GenericDO
        },
        {
            "name": "Terminal Action Code - Default",
            "description": "Specifies the acquirer’s conditions that cause a transaction to be rejected if it might "
                           "have been approved online, but the terminal is unable to process the transaction online",
            "source": "Terminal",
            "format": "b",
            "template": None,
            "tag": None,
            "length": "5",
            "object": TerminalVerificationResults
        },
        {
            "name": "Terminal Action Code - Denial",
            "description": "Specifies the acquirer’s conditions that cause the denial of a transaction without "
                           "attempt to go online",
            "source": "Terminal",
            "format": "b",
            "template": None,
            "tag": None,
            "length": "5",
            "object": TerminalVerificationResults
        },
        {
            "name": "Terminal Action Code - Online",
            "description": "Specifies the acquirer’s conditions that cause a transaction to be transmitted online",
            "source": "Terminal",
            "format": "b",
            "template": None,
            "tag": None,
            "length": "5",
            "object": TerminalVerificationResults
        },
        {
            "name": "Terminal Capabilities",
            "description": "Indicates the card data input, CVM, and security capabilities of the terminal",
            "source": "Terminal",
            "format": "b",
            "template": None,
            "tag": "9F33",
            "length": "3"
        },
        {
            "name": "Terminal Country Code",
            "description": "Indicates the country of the terminal, represented according to ISO 3166",
            "source": "Terminal",
            "format": "n 3",
            "template": None,
            "tag": "9F1A",
            "length": "2",
            "object": CountryCode
        },
        {
            "name": "Terminal Floor Limit",
            "description": "Indicates the floor limit in the terminal in conjunction with the AID",
            "source": "Terminal",
            "format": "b",
            "template": None,
            "tag": "9F1B",
            "length": "4",
            "object": GenericDO
        },
        {
            "name": "Terminal Identification",
            "description": "Designates the unique location of a terminal at a merchant",
            "source": "Terminal",
            "format": "an 8",
            "template": None,
            "tag": "9F1C",
            "length": "8",
            "object": GenericDO
        },
        {
            "name": "Terminal Risk Management Data",
            "description": "Application-specific value used by the card for risk management purposes",
            "source": "Terminal",
            "format": "b",
            "template": None,
            "tag": "9F1D",
            "length": "1-8",
            "object": GenericDO
        },
        {
            "name": "Terminal Type",
            "description": "Indicates the environment of the terminal, its communications capability, and its "
                           "operational control",
            "source": "Terminal",
            "format": "n 2",
            "template": None,
            "tag": "9F35",
            "length": "1",
            "object": TerminalType
        },
        {
            "name": "Terminal Verification Results",
            "description": "Status of the different functions as seen from the terminal",
            "source": "Terminal",
            "format": "b",
            "template": None,
            "tag": "95",
            "length": "5",
            "object": TerminalVerificationResults
        },
        {
            "name": "Threshold Value for Biased Random",
            "description": "Selection Value used in terminal risk management for random transaction selection",
            "source": "Terminal",
            "format": None,
            "template": None,
            "tag": None,
            "length": None,
            "object": GenericDO
        },
        {
            "name": "Track 1 Discretionary Data",
            "description": "Discretionary part of track 1 according to ISO/IEC 7813",
            "source": "ICC",
            "format": "ans",
            "template": "70 or 77",
            "tag": "9F1F",
            "length": "var."
        },
        {
            "name": "Track 2 Discretionary Data",
            "description": "Discretionary part of track 2 according to ISO/IEC 7813",
            "source": "ICC",
            "format": "cn",
            "template": "70 or 77",
            "tag": "9F20",
            "length": "var.",
            "object": GenericDO
        },
        {
            "name": "Track 2 Equivalent Data",
            "description": "Contains the data elements of track 2 according to ISO/IEC 7813, excluding start "
                           "sentinel, end sentinel, and Longitudinal Redundancy Check (LRC), as follows: "
                           "<ul><li>Primary Account Number n</li>"
                           "<li>Field Separator (Hex 'D')</li>"
                           "<li>Expiration Date (YYMM) n 4</li>"
                           "<li>Service Code n 3</li>"
                           "<li>Discretionary Data (defined by individual payment systems)</li>"
                           "<li>Pad with one Hex 'F' if needed to ensure whole bytes</li></ul>",
            "source": "ICC",
            "format": "b",
            "template": "70 or 77",
            "tag": "57",
            "length": "var. up to 19"
        },
        {
            "name": "Transaction Amount",
            "description": "Clearing amount of the transaction, including tips and other adjustments",
            "source": "Terminal",
            "format": "n 12",
            "template": None,
            "tag": None,
            "length": "6",
            "object": GenericDO
        },
        {
            "name": "Transaction Certificate Data Object List (TDOL)",
            "description": "List of data objects (tag and length) to be used by the terminal in generating the TC "
                           "Hash Value",
            "source": "ICC",
            "format": "b",
            "template": "70 or 77",
            "tag": "97",
            "length": "var. up to 252"
        },
        {
            "name": "Transaction Certificate (TC) Hash Value",
            "description": "Result of a hash function specified in Book 2, Annex B3.1",
            "source": "Terminal",
            "format": "b",
            "template": None,
            "tag": "98",
            "length": "20",
            "object": GenericDO
        },
        {
            "name": "Transaction Currency Code",
            "description": "Indicates the currency code of the transaction according to ISO 4217",
            "source": "Terminal",
            "format": "n 3",
            "template": None,
            "tag": "5F2A",
            "length": "2",
            "object": CurrencyCode
        },
        {
            "name": "Transaction Currency Exponent",
            "description": "Indicates the implied position of the decimal point from the right of the transaction "
                           "amount represented according to ISO 4217",
            "source": "Terminal",
            "format": "n 1",
            "template": None,
            "tag": "5F36",
            "length": "1",
            "object": GenericDO
        },
        {
            "name": "Transaction Date",
            "description": "Local date that the transaction was authorised",
            "source": "Terminal",
            "format": "n 6 YYMMDD",
            "template": None,
            "tag": "9A",
            "length": "3",
            "object": GenericDO
        },
        {
            "name": "Transaction Personal Identification Number (PIN) Data",
            "description": "Data entered by the cardholder for the purpose of the PIN verification",
            "source": "Terminal",
            "format": "b",
            "template": None,
            "tag": "99",
            "length": "var."
        },
        {
            "name": "Transaction Reference Currency Code",
            "description": "Code defining the common currency used by the terminal in case the Transaction Currency "
                           "Code is different from the Application Currency Code",
            "source": "Terminal",
            "format": "n 3",
            "template": None,
            "tag": "9F3C",
            "length": "2",
            "object": CurrencyCode
        },
        {
            "name": "Transaction Reference Currency Conversion",
            "description": "Factor used in the conversion from the Transaction Currency Code to the Transaction "
                           "Reference Currency Code",
            "source": "Terminal",
            "format": "n 8",
            "template": None,
            "tag": None,
            "length": "4",
            "object": GenericDO
        },
        {
            "name": "Transaction Reference Currency Exponent",
            "description": "Indicates the implied position of the decimal point from the right of the transaction "
                           "amount, with the Transaction Reference Currency Code represented according to ISO 4217",
            "source": "Terminal",
            "format": "n 1",
            "template": None,
            "tag": "9F3D",
            "length": "1",
            "object": GenericDO
        },
        {
            "name": "Transaction Sequence Counter",
            "description": "Counter maintained by the terminal that is incremented by one for each transaction",
            "source": "Terminal",
            "format": "n 4-8",
            "template": None,
            "tag": "9F41",
            "length": "2-4",
            "object": GenericDO
        },
        {
            "name": "Transaction Status Information",
            "description": "Indicates the functions performed in a transaction",
            "source": "Terminal",
            "format": "b",
            "template": None,
            "tag": "9B",
            "length": "2",
            "object": TransactionStatusInformation
        },
        {
            "name": "Transaction Time",
            "description": "Local time that the transaction was authorised",
            "source": "Terminal",
            "format": "n 6 HHMMSS",
            "template": None,
            "tag": "9F21",
            "length": "3",
            "object": GenericDO
        },
        {
            "name": "Transaction Type",
            "description": "Indicates the type of financial transaction, represented by the first two digits of the "
                           "ISO 8583:1987 Processing Code. The actual values to be used for the Transaction Type data "
                           "element are defined by the relevant payment system",
            "source": "Terminal",
            "format": "n 2",
            "template": None,
            "tag": "9C",
            "length": "1",
            "object": TransactionType
        },
        {
            "name": "Unpredictable Number",
            "description": "Value to provide variability and uniqueness to the generation of a cryptogram",
            "source": "Terminal",
            "format": "b",
            "template": None,
            "tag": "9F37",
            "length": "4",
            "object": GenericDO
        },
        {
            "name": "Upper Consecutive Offline Limit",
            "description": "Issuer-specified preference for the maximum number of consecutive offline transactions "
                           "for this ICC application allowed in a terminal without online capability",
            "source": "ICC",
            "format": "b",
            "template": "70 or 77",
            "tag": "9F23",
            "length": "1",
            "object": HexNumericDO
        },
    ]

    data_type = [
        {
            "type": "a",
            "name": "Alphabetic",
            "description": "Alphabetic data elements contain a single character per byte.The "
                           "permitted characters are alphabetic only(a to z and A to Z, upper and lower case)."
        },
        {
            "type": "an",
            "name": "Alphanumeric",
            "description": "Alphanumeric data elements contain a single character per byte. The permitted "
                           "characters are alphabetic(a to z and A to Z, upper and lower case) and numeric(0 to 9)."
        },
        {
            "type": "ans",
            "name": "Alphanumeric Special",
            "description": "Alphanumeric Special data elements contain a single character per byte. The permitted "
                           "characters and their coding are shown in the Common Character Set table in Annex B of "
                           "Book 4.<br/>"
                           "There is one exception: The permitted characters for Application Preferred Name are the "
                           "non-control characters defined in the ISO / IEC 8859 part designated in the Issuer Code "
                           "Table Index associated with the Application Preferred Name."
        },
        {
            "type": "b",
            "name": "binary",
            "description": "These data elements consist of either unsigned binary numbers or bit combinations that "
                           "are defined elsewhere in the specification.<br/>"
                           "Binary example: The Application Transaction Counter(ATC) is defined as “b” with a "
                           "length of two bytes.An ATC value of 19 is stored as Hex '00 13'.<br/>"
                           "Bit combination example: Processing Options Data Object List(PDOL) is defined as “b”"
                           "with the format shown in section 5.4."
        },
        {
            "type": "cn",
            "name": "Compressed Numeric",
            "description": "Compressed numeric data elements consist of two numeric digits (having values in the range "
                           "Hex '0'–'9') per byte.These data elements are left justified and padded with trailing "
                           "hexadecimal 'F's.<br/>"
                           "Example: The Application Primary Account Number(PAN) is defined as “cn” with a length of "
                           "up to ten bytes.A value of 1234567890123 may be stored in the Application PAN as Hex "
                           "'12 34 56 78 90 12 3F FF' with a length of 8."
        },
        {
            "type": "n",
            "name": "Numeric",
            "description": "Numeric data elements consist of two numeric digits (having values in the range Hex "
                           "'0' – '9') per byte.These digits are right justified and padded with leading hexadecimal "
                           "zeroes.Other specifications sometimes refer to this data format as Binary Coded Decimal "
                           "(“BCD”) or unsigned packed.<br/>"
                           "Example: Amount, Authorised(Numeric) is defined as “n 12” with a length of six bytes.A "
                           "value of 12345 is stored in Amount, Authorised (Numeric) as Hex '00 00 00 01 23 45'."
        },
        {
            "type": "var.",
            "name": "Variable",
            "description": "Variable data elements are variable length and may contain any bit combination.Additional "
                           "information on the formats of specific variable data elements is available elsewhere"
        }
    ]

    @staticmethod
    def find_do_by_tag(tag):
        if tag is None:
            return None
        for do in DataObjectDefinitions.dictionary:
            if do["tag"] is None:
                continue
            if do["tag"].lower() == str(tag).lower():
                return do
        return None
