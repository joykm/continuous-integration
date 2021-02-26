def my_func():
    return "Hello World"


def conv_num(num_str):

    result = 0

    # convert int string to int by using the ascii code of the char
    # subtracted from the ascii code for 0. Each iteration multiply
    # by 10 to move the decimal place over.
    for char in num_str:
        result = result * 10 + ord(char) - ord('0')

    return result
