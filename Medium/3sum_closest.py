def threeSumClosest(nums, target):
    n = len(nums)
    result = None
    best = float('inf')
    if n > 2:
        nums = sorted(nums)
        for i in range(n-2):
            j, k = i+1, n-1
            while j < k:
                summation = nums[i] + nums[j] + nums[k]
                difference = abs(target-summation)
                if difference < best:
                    result = summation
                    best = difference
                if summation > target:
                    k -= 1
                else:
                    j += 1
    return result


if __name__ == "__main__":
    assert(threeSumClosest([-1, 2, 1, -4], 1) == 2)