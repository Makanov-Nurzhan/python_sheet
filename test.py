def spiralTraverse(array):
    res = []
    sR = 0
    eR = len(array) - 1
    sC = 0
    eC = len(array[0]) - 1
    while sR <= eR and sC <= eC:
        for i in range(sC, eC + 1):
            res.append(array[sR][i])
        for j in range(sR + 1, eR + 1):
            res.append(array[j][eC])
        for i in reversed(range(sC, eC)):
            if sR == eR:
                break
            res.append(array[eR][i])
        for j in reversed(range(sR + 1, eR)):
            if sC == eC:
                break
            res.append(array[j][sC])
        sR += 1
        eR -= 1
        sC += 1
        eC -= 1
    return res


def isPalindrome(string):
    l = 0
    r = len(string) - 1
    isP = True
    if len(string) < 2:
        return isP
    while l < r:
        if string[l] == string[r]:
            isP = True
            l += 1
            r -= 1
        else:
            return False
    return isP


def longestPeak(array):
    peakLenth = 0
    isPeak = 0
    i = 1
    while i < len(array) - 1:
        isPeak = array[i] > array[i - 1] and array[i] > array[i + 1]
        if not isPeak:
            i += 1
            continue

        left = i - 2
        while left >= 0 and array[left] < array[left + 1]:
            left -= 1
        right = i + 2
        while right < len(array) and array[right] < array[right - 1]:
            right += 1
        currLenth = right - left
        peakLenth = max(currLenth, peakLenth)
        i = right
    return peakLenth


def firstDuplicateValue(array):
    map = {}
    for i in range(len(array)):
        if array[i] in map:
            dis = i
            continue
        map[array[i]] = i


def firstDuplicateValue(array):
    for i in array:
        absV = abs(i)
        if array[absV - 1] < 0:
            return absV
        array[absV - 1] *= -1
    return -1


def findThreeLargestNumbers(array):
    firstMax, secondMax, thirdMax = float("-inf"), float("-inf"), float("-inf")
    for i in range(len(array)):
        if array[i] > firstMax:
            thirdMax = secondMax
            secondMax = firstMax
            firstMax = array[i]
        elif array[i] > secondMax:
            thirdMax = secondMax
            secondMax = array[i]
        elif array[i] > thirdMax:
            thirdMax = array[i]

    return [thirdMax, secondMax, firstMax]


def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
    return array


def fourNumberSum(array, targetSum):
    res = []
    map = {}
    for i in range(1, len(array) - 1):
        for j in range(i + 1, len(array)):
            sum = array[j] + array[i]
            com = targetSum - sum
            if com in map:
                for p in map[com]:
                    res.append(p + [array[i], array[j]])
        for k in range(0, i):
            sum = array[i] + array[k]
            if sum not in map:
                map[sum] = [[array[k], array[i]]]
            else:
                map[sum].append([array[k], array[i]])

    return res


def mergeOverlappingIntervals(intervals):
    res = []
    sortedInt = sorted(intervals, key=lambda x: x[0])
    currentInt = sortedInt[0]
    res.append(currentInt)

    for nextInt in sortedInt:
        _, currentIntEnd = currentInt
        nextIntStart, nextIntEnd = nextInt

        if currentIntEnd >= nextIntStart:
            currentInt[1] = max(currentIntEnd, nextIntEnd)
        else:
            currentInt = nextInt
            res.append(currentInt)

    return res


def bestSeat(seats):
    maxEmpty = 0
    seat = -1
    l = 0

    while l < len(seats):
        r = l + 1
        while r < len(seats) and seats[r] == 0:
            r += 1
        availSp = r - l - 1
        if availSp > maxEmpty:
            seat = (r + l) // 2
            maxEmpty = availSp
        l = r
    return seat


def zeroSumSubarray(nums):
    curSum = 0
    map = {0: 0}
    for i in range(len(nums)):
        curSum += nums[i]
        if curSum in map:
            return True
        map[nums[i]] = i
    return False


def missingNumbers(nums):
    n = set(nums)
    res = []
    d = len(nums) + 2
    i = 1
    while i <= d:
        if i not in n:
            res.append(i)
        i += 1
    return res


def majorityElement(array):
    count = 0
    major = None

    for i in array:
        if count == 0:
            major = i
        if i == major:
            count += 1
        else:
            count -= 1
    return major


def sweetAndSavory(dishes, target):
    sweet = sorted([i for i in dishes if i < 0], key=abs)
    savor = sorted([i for i in dishes if i > 0])
    res = [0, 0]
    differ = float("inf")
    sweetIdx, savorIdx = 0, 0
    while sweetIdx < len(sweet) and savorIdx < len(savor):
        curSum = sweet[sweetIdx] + savor[savorIdx]
        if curSum <= target:
            curDiffer = target - curSum
            if curDiffer < differ:
                differ = curDiffer
                res = [sweet[sweetIdx], savor[savorIdx]]
            savorIdx += 1
        else:
            sweetIdx += 1
    return res


array = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
]


def searchInSortedMatrix(matrix, target):
    sR = 0
    eC = len(matrix[0]) - 1
    while sR < len(matrix) and eC >= 0:
        if matrix[sR][eC] > target:
            eC -= 1
        elif matrix[sR][eC] < target:
            sR += 1
        else:
            return [sR, eC]
    return [-1, -1]
