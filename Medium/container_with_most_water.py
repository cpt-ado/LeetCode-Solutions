def maxArea(height):
    n = len(height)
    i, j = 0, n-1
    best = 0
    while i < j:
        if height[i] < height[j]:
            b = i
            temp = height[i] * (j-i)
            while i < n-1 and height[b] >= height[i]:
                i += 1
        else:
            b = j
            temp = height[j] * (j-i)
            while j > 0 and height[b] >= height[j]:
                j -= 1
        if best < temp:
            best = temp
    return best
        



if __name__ == "__main__":
    assert(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49)
    assert(maxArea([1, 1]) == 1)
    assert(maxArea([4, 3, 2, 1, 4]) == 16)
    assert(maxArea([1, 2, 1]) == 2)