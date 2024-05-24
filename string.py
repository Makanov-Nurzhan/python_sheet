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
