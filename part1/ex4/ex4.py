def hex_output(a):
    raw = str(a)
    result = 0
    index = 0
    for c in raw[-1 : -len(raw) - 1 : -1]:
        result += int(c) * pow(16, index)
        index += 1
    return result
