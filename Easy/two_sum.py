def twoSum(nums, target):
        data = {}
        for j in range(len(nums)):
            i = data.get(target - nums[j], None)
            if i is None:
                data[nums[j]] = j
            else:
                return [i, j]


if __name__ == '__main__':
    assert(twoSum([2, 7, 11, 15], 9) == [0, 1])
    assert(twoSum([3, 2, 4], 6) == [1, 2])
    assert(twoSum([3, 3], 6) == [0, 1])