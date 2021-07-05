UPPER_LIMIT = 2 ** 31 - 1
LOWER_LIMIT = -2 ** 31


def myAtoi(s):
    result = 0

    # ignore leading space character
    while s and s[0] == ' ':
        s = s[1:]

    # check the sign
    sign = 1
    if s:
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

    # read digit characters
    digits = ''
    for c in s:
        if c.isnumeric():
            digits += c
        else:
            break

    # convert to int
    if digits:
        result = sign * int(digits)
    
    # check range
    if result > UPPER_LIMIT:
        return UPPER_LIMIT
    elif result < LOWER_LIMIT:
        return LOWER_LIMIT
    return result      


if __name__ == '__main__':
    # assert(myAtoi("42") == 42)
    assert(myAtoi("   -42") == -42)
    assert(myAtoi("4193 with words") == 4193)
    assert(myAtoi("words and 987") == 0)
    assert(myAtoi("-91283472332") == -2147483648)