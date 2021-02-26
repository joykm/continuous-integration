def my_func():
    return "Hello World"


def conv_num(num_str):

    # check if input is valid format
    if num_str == '':
        return None

    dec_point_found = False
    dec_len = 0
    integer = 0
    decimal = 0
    result = 0

    for i in range(len(num_str)):

        if num_str[i] == ".":
            dec_point_found = True
            dec_len = len(num_str) - (i + 1)
            continue

        if dec_point_found is False:
            integer = integer * 10 + ord(num_str[i]) - ord('0')
        else:
            decimal = decimal * 10 + ord(num_str[i]) - ord('0')

    decimal = decimal / (10 ** dec_len)
    result = integer + decimal

    return result
