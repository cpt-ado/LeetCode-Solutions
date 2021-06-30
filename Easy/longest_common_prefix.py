def longestCommonPrefix(strs):
    result = ""
    n = min([len(s) for s in strs])
    i = 0
    while i < n:
        if all(s[i] == strs[0][i] for s in strs):
            result += strs[0][i]
        else:
            return result
        i += 1
    return result


if __name__ == '__main__':
    assert(longestCommonPrefix(["flower","flow","flight"]) == 'fl')
    assert(longestCommonPrefix(["dog","racecar","car"]) == '')