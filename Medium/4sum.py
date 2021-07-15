def fourSum(nums, target):
    n = len(nums)
    result = []
    if n > 3:
        nums = sorted(nums)
        for i in range(n-3):
            if i and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-2):
                if j != i+1 and nums[j] == nums[j-1]:
                    continue
                t = target - nums[i] - nums[j]
                k, l = j+1, n-1
                while k < l:
                    if nums[k] + nums[l] > t:
                        l -= 1
                    elif nums[k] + nums[l] < t:
                        k += 1
                    else:
                        result.append([nums[i],
                                       nums[j],
                                       nums[k],
                                       nums[l]])
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k-1]:
                            k += 1
                        while k < l and nums[l] == nums[l+1]:
                            l -= 1
    return result


if __name__ == "__main__":
    assert(fourSum([], 1) == [])
    assert(fourSum([0], 255) == [])
    assert(fourSum([2, 2, 2, 2, 2], 8) == [[2, 2, 2, 2]])
    assert(fourSum([1, 0, -1, 0, -2, 2], 0) == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]])