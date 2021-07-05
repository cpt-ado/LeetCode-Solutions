def removeDuplicates(nums):
    db = {}
    i = 0
    for n in nums:
        if db.get(n, False):
            continue
        db[n] = True
        nums[i] = n
        i += 1
    return i


if __name__ == '__main__':
    nums = [1, 1, 2]
    n = removeDuplicates(nums)
    assert(n == 2)
    expected = [1, 2, 2]
    for i in range(n):
        assert(nums[i] == expected[i])

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    n = removeDuplicates(nums)
    assert(n == 5)
    expected = [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
    for i in range(n):
        assert(nums[i] == expected[i])