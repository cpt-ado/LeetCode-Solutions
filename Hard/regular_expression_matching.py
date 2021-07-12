def isMatch(sequence, pattern):
    n_s = len(sequence) + 1
    n_p = len(pattern) + 1
    matrix = [[False for _ in range(n_p)] for _ in range(n_s)]
    matrix[0][0] = True
    for p in range(2, n_p, 2):
        if matrix[0][p-2] and pattern[p-1] == '*':
            matrix[0][p] = True
        else:
            break
    for s in range(1, n_s):
        for p in range(1, n_p):
            if pattern[p-1] == '*':
                if sequence[s-1] == pattern[p-2] or pattern[p-2] == '.':
                    matrix[s][p] =  matrix[s-1][p] or matrix[s][p-2]
                else:
                    matrix[s][p] = matrix[s][p-2]
            else:
                if sequence[s-1] == pattern[p-1] or pattern[p-1] == '.':
                    matrix[s][p] = matrix[s-1][p-1]
    return matrix[-1][-1]


if __name__ == '__main__':
    assert(isMatch("", "") == True)
    assert(isMatch("", "a*b*") == True)
    assert(isMatch("", "a") == False)
    assert(isMatch("a", "a") == True)
    assert(isMatch("a", "b*") == False)
    assert(isMatch("a", ".") == True)
    assert(isMatch("aa", ".") == False)
    assert(isMatch("aa", "a") == False)
    assert(isMatch("aa", "a*") == True)
    assert(isMatch("ab", ".*") == True)
    assert(isMatch("aab", "c*a*b") == True)
    assert(isMatch("mississippi", "mis*is*p*") == False)
    assert(isMatch("mississippi", "mis*is*ip*.") == True)