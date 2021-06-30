ROMAN_TO_INTEGER = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


def romanToInt(s):
    result = 0
    prev = ROMAN_TO_INTEGER[s[-1]]
    for c in s[::-1]:
        curr = ROMAN_TO_INTEGER[c]
        if curr < prev:
            result -= curr
        else:
            result += curr
        prev = curr
    return result


if __name__ == '__main__':
    assert(romanToInt("III") == 3)
    assert(romanToInt("IV") == 4)
    assert(romanToInt("IX") == 9)
    assert(romanToInt("LVIII") == 58)
    assert(romanToInt("MCMXCIV") == 1994)