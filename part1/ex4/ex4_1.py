def get_hex_digit(hex_digit: str):
    code_point = ord(hex_digit)
    if (
        (code_point >= 48 and code_point <= 57)
        or (code_point >= 65 and code_point <= 70)
        or (code_point >= 97 and code_point <= 102)
    ):
        return int(hex_digit, 16)
    raise ValueError("The digit is not valid")


def hex_output(hex_num: str):
    result = 0
    for index, value in enumerate(reversed(hex_num)):
        result += get_hex_digit(value) * pow(16, index)
    return result
