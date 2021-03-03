from math import floor
import re


def is_string_valid(num_str):
    string_valid = True
    # check if input is empty
    if num_str == '':
        string_valid = False

    # check for repeat the key characters
    if num_str.count('0X') > 1 or num_str.count('0x') > 1 or \
            num_str.count('-') > 1 or num_str.count('.') > 1:
        string_valid = False

    return string_valid


def conv_num(num_str):

    # check for initial validation
    if is_string_valid(num_str) is False:
        return None

    result = 0
    is_negative = False

    # check if input is a negative value
    # strip input and replace "-" with "" (empty character)
    if num_str[0] == "-":
        num_str = num_str.replace('-', "")
        is_negative = True

    # if string start with 0x or 0X
    # Start hexadecimal convert to decimal
    if num_str.startswith(('0x', '0X',)):

        # strip '0x' or '0X' out before the conversion
        stripped_num_str = None
        if '0x' in num_str:
            stripped_num_str = num_str.replace('0x', "")

        elif '0X' in num_str:
            stripped_num_str = num_str.replace('0X', "")

        # Create a conversion table
        conversion_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                            '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                            'A': 10, 'B': 11, 'C': 12, 'D': 13,
                            'E': 14, 'F': 15, 'a': 10, 'b': 11,
                            'c': 12, 'd': 13, 'e': 14, 'f': 15}

        # get exponential degree
        exp_degree = len(stripped_num_str) - 1

        # iterate through each character to lookup 'conversion_table'
        # adding results for each character
        # return None if not in conversion map
        # decrement of exponential degree
        for c in stripped_num_str:
            try:
                result += conversion_table[c] * (16 ** exp_degree)
                exp_degree -= 1
            except KeyError:
                return None

        # check for negative string input returns negative value
        if is_negative:
            result = result * (-1)

    else:
        # convert decimal string to decimal
        # initialize variables
        dec_point_found = False
        dec_len = 0
        integer = 0
        decimal = 0
        char_allowed = re.compile('[.0123456789]')

        for i in range(len(num_str)):

            # check for any character not allow
            if not char_allowed.search(num_str[i]):
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


# given seconds since epoch, return 'mm-dd-yyyy'
def my_datetime(num_sec):

    # initiate variables
    sec_in_day = 86400
    year = 1970
    is_ly = False
    month = 1
    day = 1

    # day ranges in a normal year for each month jan through dec respectively
    non_ly_day_ranges = {1: 32, 2: 60, 3: 91, 4: 121, 5: 152, 6: 182, 7: 213,
                         8: 244, 9: 274, 10: 305, 11: 335, 12: 366}

    # day ranges in a normal year for each month jan through dec respectively
    ly_day_ranges = {1: 32, 2: 61, 3: 92, 4: 122, 5: 153, 6: 183, 7: 214,
                     8: 245, 9: 275, 10: 306, 11: 336, 12: 367}

    # find days since epoch
    day_count = floor(num_sec / sec_in_day)

    # find year
    while (day_count > 365 and not is_ly) or (day_count > 366 and is_ly):
        if is_ly:
            day_count -= 366
            day += 366
            year += 1
        else:
            day_count -= 365
            day += 365
            year += 1

        # set is_ly
        is_ly = (year % 4 == 0 and year % 100 != 0) or \
                (year % 4 == 0 and year % 400 == 0)

    # determine if we are in a leap year, and find month
    # we are in given days into year. Add 1 to day count
    # because if we have 58 full days we are in the 59th day of the year.
    prev_month_end = 1
    day = day_count + 1
    if is_ly:
        for m in ly_day_ranges:
            if day > (ly_day_ranges[m] - prev_month_end):
                day -= (ly_day_ranges[m] - prev_month_end)
            else:
                month = m
                break
            prev_month_end = ly_day_ranges[m]
    else:
        for m in non_ly_day_ranges:
            if day > (non_ly_day_ranges[m] - prev_month_end):
                day -= (non_ly_day_ranges[m] - prev_month_end)
            else:
                month = m
                break
            prev_month_end = non_ly_day_ranges[m]

    # zero fill day if needed
    day_str = str(day)
    if len(day_str) < 2:
        day_str = day_str.zfill(2)

    # zero fill month if needed
    month_str = str(month)
    if len(month_str) < 2:
        month_str = month_str.zfill(2)

    # format date string
    date = month_str + "-" + day_str + "-" + str(year)

    return date


# Function 3
def conv_endian(num, endian="big"):
    # map to assist with conversion
    hex_map = {
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
        8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
    }

    # list to contain chars of converted numbers
    bytes = []

    # check if we have are on the first half of the byte from left to right
    left_half = False
    # the current byte
    prev = ""

    # each hex place is 0 to 15
    # if last digit is smaller than 16 we break out of the loop
    while not num/16 == 0:
        curr = hex_map[num % 16]
        # when we have the full byte we append to the list
        if left_half:
            bytes.append(curr + prev)
            left_half = False
        # if we only have the first byte we save it for later
        else:
            prev = curr
            left_half = True
        # divide to continue to next digit
        num = floor(num / 16)
    # if the loop quit early append zero to the right_half
    if left_half:
        bytes.append("0" + prev)

    # default output is little endian
    if endian != "little":
        bytes = bytes[::-1]
    return " ".join(bytes)
