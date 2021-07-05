def lengthOfLongestSubstring(s):
    i, j = 0, 1
    count = {}
    output = [0,]
    while j <= len(s):
        count[s[j-1]] = count.get(s[j-1], 0) + 1
        if count[s[j-1]] == 1:
            output.append(j-i)
        else:
            while count.get(s[j-1], 0) > 1:
                count[s[i]] -= 1
                i += 1
        j += 1
    return max(output)


if __name__ == '__main__':
    assert(lengthOfLongestSubstring("abcabcbb") == 3)
    assert(lengthOfLongestSubstring("bbbbb") == 1)
    assert(lengthOfLongestSubstring("pwwkew") == 3)
    assert(lengthOfLongestSubstring("") == 0)