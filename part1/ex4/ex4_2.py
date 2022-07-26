def calc_lines(name: str):
    length = len(name)
    if length == 0:
        return 0
    line_count = 1
    while length > 1:
        length -= line_count
        line_count += 1
    return line_count


def print_name(name: str):
    line_count = calc_lines(name)
    max_line_length = (line_count) - 1 * 2
    for i in range(line_count + 1):
        pass
