def hex_output(hex_num: str):
    result = 0
    for index, value in enumerate(reversed(hex_num)):
        result += int(value, 16) * pow(16, index)
    return result
