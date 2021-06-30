def reverse(x):
    sign = 1
    if x < 0:
        sign = -1
        x *= sign
    solution = 0
    while x > 0:
        solution *= 10
        solution += x % 10
        x = x // 10
    solution *= sign
    limit = 2 ** 31
    if solution >= limit or solution < -limit:
        return 0
    return solution


if __name__ == '__main__':
    assert(reverse(123) == 321)
    assert(reverse(-123) == -321)
    assert(reverse(120) == 21)
    assert(reverse(0) == 0)