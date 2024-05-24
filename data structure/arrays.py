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


def tournamentWinner(competitions, results):
    curWinner = ""
    map = {curWinner: 0}
    for i, j in enumerate(competitions):
        homeT, anyT = j
        winningTeam = homeT if results[i] == 1 else anyT
        if winningTeam not in map:
            map[winningTeam] = 0
        map[winningTeam] += 3
        if map[winningTeam] > map[curWinner]:
            curWinner = winningTeam
    return curWinner


def subarraySort(array):
    left, right = -1, -1
    maxval = array[0]
    for i, el in enumerate(array):
        if el < maxval:
            left = i
        else:
            maxval = el
    minval = array[-1]
    for i, el in reversed(list(enumerate(array))):
        if el > minval:
            right = i
        else:
            minval = el
    return [right, left]


def largestRange(array):
    res = []
    n = set(array)
    maxLenth = 0
    for i in array:
        if (i - 1) not in n:
            k = i
            while k in n:
                k += 1
            lenth = k - i
            if lenth > maxLenth:
                maxLenth = lenth
                res = [i, k - 1]

    return res, maxLenth


scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]


def minRewards(scores):
    res = [1 for _ in scores]
    for i in range(1, len(scores)):
        j = i - 1
        if scores[i] > scores[j]:
            res[i] = res[j] + 1
        else:
            while j >= 0 and scores[j] > scores[j + 1]:
                res[j] = max(res[j], res[j + 1] + 1)
                j -= 1
    return sum(res)


def minRewards1(scores):
    res = [1 for _ in scores]
    for i in range(1, len(scores)):
        if scores[i] > scores[i - 1]:
            res[i] = res[i - 1] + 1
    for i in reversed(range(len(scores) - 1)):
        if scores[i] > scores[i + 1]:
            res[i] = max(res[i], res[i + 1] + 1)
    return sum(res)


def getNthFib(n):
    i1 = 0
    i2 = 1
    nextN = i2
    count = 1
    while count <= n:
        count += 1
        i1, i2 = i2, nextN
        nextN = i1 + i2
    return nextN


def getNthFib1(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return (getNthFib1(n - 1) + getNthFib1(n - 2))


def powerset(array):
    sub = [[]]
    for el in array:
        for i in range(len(sub)):
            curSub = sub[i]
            sub.append(curSub + [el])
    return sub
