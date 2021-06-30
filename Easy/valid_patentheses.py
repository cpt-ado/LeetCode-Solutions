PAIR = {
    '(': ')',
    '{': '}',
    '[': ']',
}

OPEN = {'(', '[', '{'}


def isValid(s):
    next = [None]
    for c in s:
        if c in PAIR.keys():
            next.append(PAIR[c])
        else:
            if c == next[-1]:
                next.pop()
            else:
                return False
    if next[-1] is None:
        return True
    return False


if __name__ == '__main__':
    assert(isValid("(") == False)
    assert(isValid("()") == True)
    assert(isValid("()[]{}") == True)
    assert(isValid("(]") == False)
    assert(isValid("([)]") == False)
    assert(isValid("([])(") == False)
    assert(isValid("{[]}") == True)