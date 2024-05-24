time = [3, 2, 1, 2, 6]


def minimumWaitingTime1(time):
    time.sort()
    runSum = prev = 0
    for i in time:
        runSum += prev
        prev += i
    return runSum


def minimumWaitingTime(time):
    time.sort()
    sum = 0
    for i in range(len(time)):
        tmp = len(time) - (i + 1)
        sum += time[i] * tmp
    return sum


def tree(p, v, q, m):
    startV = (p - v)
    endV = (p + v)
    startM = (q - m)
    endM = (q + m)
    start = min(startV, startM)
    end = max(endV, endM)
    if endV >= startM and startV <= endM:
        return end - start + 1
    else:
        return (endV - startV + 1) + (endM - startM + 1)
