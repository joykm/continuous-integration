from math import floor


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


def my_datetime(num_sec):

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
        is_ly = (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 400 == 0)

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

    date = month_str + "-" + day_str + "-" + str(year)
    print(date)

    return date
