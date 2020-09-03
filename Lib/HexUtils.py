def is_all_bcd(value):
    for x in value:
        if x < 0x30 or x > 0x39:
            return False
    return True
