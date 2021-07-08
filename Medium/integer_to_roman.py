def intToRoman(num):
    roman = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }
    integer = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    result = ''
    while num > 0:
        while integer[-1] > num:
            integer.pop()
        num -= integer[-1]
        result += roman[integer[-1]]
    return result


if __name__ == "__main__":
    assert(intToRoman(3) == "III")
    assert(intToRoman(4) == "IV")
    assert(intToRoman(9) == "IX")
    assert(intToRoman(58) == "LVIII")
    assert(intToRoman(1994) == "MCMXCIV")

    assert(intToRoman(685) == "DCLXXXV")
    assert(intToRoman(104) == "CIV")
    assert(intToRoman(777) == "DCCLXXVII")