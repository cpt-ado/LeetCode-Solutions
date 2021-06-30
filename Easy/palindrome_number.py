from math import log10 as log


def isPalindrome(x):
    if x < 0:
        return False
    elif x < 10:
        return True
    mod = 10 ** int(log(x))
    while mod >= 10:
        top = x%mod
        a = int((x-top)/mod)
        b = x%10
        x = int(top/10)
        if a != b:
            return False
        mod = int(mod/100)
    return True


if __name__ == '__main__':
    assert(isPalindrome(12121) == True)
    assert(isPalindrome(-121) == False)
    assert(isPalindrome(10) == False)
    assert(isPalindrome(-101) == False)
    assert(isPalindrome(1001) == True)