class ISO8583:
    dictionary = [
        {"code": "00", "description": "Goods and Services (Debit)"},
        {"code": "01", "description": "Cash (Debit)"},
        {"code": "02", "description": "Adjustment (Debit)"},
        {"code": "03", "description": "Check Guarantee (Debit)"},
        {"code": "04", "description": "Check Verification (Debit)"},
        {"code": "05", "description": "Eurocheque (Debit)"},
        {"code": "06", "description": "Travelers Check (Debit)"},
        {"code": "07", "description": "Letter of Credit (Debit)"},
        {"code": "08", "description": "Giro (Postal Banking) (Debit)"},
        {"code": "09", "description": "Goods and Services with Cash Disbursement (Debit)"},
        {"code": "0A", "description": "Phone Top-Up (Private)"},
        {"code": "0B", "description": "Fee Collection (Debit)"},
        {"code": "10", "description": "Non-cash Financial Instrument (Debit)"},
        {"code": "11", "description": "Quasi-cash and Scrip (Debit)"},
        {"code": "17", "description": "Fast Cash (Debit)"},
        {"code": "18", "description": "Private Use (Debit)"},
        {"code": "19", "description": "Private Use (Debit)"},
        {"code": "20", "description": "Return (Credit)"},
        {"code": "21", "description": "Deposit (Credit)"},
        {"code": "22", "description": "Adjustment (Credit)"},
        {"code": "23", "description": "Check Deposit Guarantee (Credit)"},
        {"code": "24", "description": "Check Deposit (Credit)"},
        {"code": "28", "description": "Deposit with Cash Back (Credit)"},
        {"code": "29", "description": "Check Deposit with Cash Back (Credit)"},
        {"code": "2A", "description": "Funds Dispursement"},
        {"code": "2A", "description": "Funds Dispursement"},
        {"code": "2B", "description": "Prepaid Load (Credit)"},
        {"code": "2C", "description": "Original Credits"},
        {"code": "2D", "description": "Cash Deposit with Cash Back"},
        {"code": "2E", "description": "Cash Deposit"},
        {"code": "2F", "description": "Split Deposit"},
        {"code": "30", "description": "Inquiry – Available Funds Inquiry"},
        {"code": "31", "description": "Inquiry – Balance Inquiry"},
        {"code": "38", "description": "Card Verification"},
        {"code": "39", "description": "Statement Print (inbound/outbound)"},
        {"code": "3A", "description": "Mini-Statement Inquiry Check Clear (inbound/outbound)"},
        {"code": "3B", "description": "Mini-Statement Inquiry Last Debit/Credit (inbound/outbound)"},
        {"code": "3C", "description": "Mini-Statement Inquiry Last Source (inbound/outbound)"},
        {"code": "3D", "description": "Mini-Statement Inquiry Last Check (inbound/outbound)"},
        {"code": "3E", "description": "Mini-Statement Inquiry Last Debit (inbound/outbound)"},
        {"code": "3F", "description": "Mini-Statement Inquiry Last Credit (inbound/outbound)"},
        {"code": "3G", "description": "Mini-Statement Inquiry Last Transfer (inbound/outbound)"},
        {"code": "3H", "description": "Inquiry – Customer Vendor"},
        {"code": "3J", "description": "Inquiry – Scheduled Payment"},
        {"code": "3J", "description": "Inquiry – Scheduled Payment"},
        {"code": "3K", "description": "Inquiry – Scheduled Transfer"},
        {"code": "3L", "description": "Inquiry – Last Payment and Transfer"},
        {"code": "3M", "description": "Inquiry – Scheduled Transaction"},
        {"code": "3N", "description": "Inquiry – Account List"},
        {"code": "40", "description": "Transfer – Cardholder Accounts Transfer"},
        {"code": "48", "description": "Transfer – Private Use"},
        {"code": "49", "description": "Transfer – Private Use"},
        {"code": "4A", "description": "Transfer – Future"},
        {"code": "4B", "description": "Transfer – Recurring"},
        {"code": "50", "description": "Payment (can include both a from and to account type)"},
        {"code": "56", "description": "Payment to (only a to account is present)"},
        {"code": "58", "description": "Payment Enclosed"},
        {"code": "59", "description": "Payment – Private Use"},
        {"code": "5A", "description": "Payment – Payment Future"},
        {"code": "5B", "description": "Payment – Recurring"},
        {"code": "5C", "description": "Bulk Authorization"},
        {"code": "5D", "description": "Return Payment"},
        {"code": "5E", "description": "Scheme Return Payment"},
        {"code": "5F", "description": "Corporate Dated Payment"},
        {"code": "5G", "description": "Payment To Third Party"},
        {"code": "5H", "description": "Payment From Third Party"},
        {"code": "90", "description": "PIN Change"},
        {"code": "91", "description": "PIN Verify"}
    ]

    @staticmethod
    def find_transaction_code(numStr=""):
        for x in ISO8583.dictionary:
            if x["code"] == numStr:
                return x
        return {"code": numStr, "description": "Unknown Transaction Type"}