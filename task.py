import re


def my_func():
    return "Hello World"


def conv_num(num_str):

    # check if input is valid format
    if num_str == '':
        return None

    # check for any character not allow
    regex = re.compile('[.xabcdefABCDEF0123456789-]')
    for i in num_str:
        if not regex.search(i):
            return None

    dec_point_found = False
    dec_len = 0
    integer = 0
    decimal = 0
    result = 0

    # check if input is a negative value
    # replace "-" with "" (empty character)
    is_negative = False
    if num_str[0] == "-":
        num_str = num_str.replace('-', "")
        is_negative = True

    for i in range(len(num_str)):

        # Determine if "-" is somewhere else, return None
        if num_str[i] == "-":
            return None

        if num_str[i] == ".":
            dec_point_found = True
            dec_len = len(num_str) - (i + 1)
            continue

        if dec_point_found is False:
            integer = integer * 10 + ord(num_str[i]) - ord('0')
        else:
            decimal = decimal * 10 + ord(num_str[i]) - ord('0')

    decimal = decimal / (10 ** dec_len)

    if is_negative:
        result = (integer + decimal) * (-1)
    else:
        result = integer + decimal

    return result
