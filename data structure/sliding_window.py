def longestSubstringWithoutDuplication(s):
    l = r = 0
    maxLen = 0
    subS = ""
    char = set()
    while (r < len(s)):
        c = s[r]
        if c not in char:
            char.add(c)
            if r - l + 1 > maxLen:
                maxLen = r - l + 1
                subS = s[l:r + 1]
            r += 1
        else:
            char.remove(s[l])
            l += 1
    return subS


arr = [1, 2, 3, 4, 3, 3, 1, 2, 1, 2]
target = 10


def longestSubArray(arr, target):
    l = 0
    curSum = 0
    res = []
    for r in range(len(arr)):
        curSum += arr[r]
        while curSum > target and l < r:
            curSum -= arr[l]
            l += 1
        if curSum == target:
            if len(res) == 0 or res[1] - res[0] < r - l:
                res = [l, r]

    return res


print(longestSubArray(arr, target))
