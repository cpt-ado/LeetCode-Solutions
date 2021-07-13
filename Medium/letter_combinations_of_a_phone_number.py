NUMBER_TO_LETTER = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}


def letterCombinations(digits):
    if len(digits) > 0:
        result = NUMBER_TO_LETTER[digits[0]]
        for n in digits[1:]:
            letters = NUMBER_TO_LETTER[n]
            temp = []
            for c in letters:
                temp = temp + [x+c for x in result]
            result = temp
        return result
    return []

if __name__ == '__main__':
    assert(letterCombinations("") == [])
    assert(letterCombinations("2") == ["a", "b", "c"])
    assert(sorted(letterCombinations("23")) == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])