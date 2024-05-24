def isPalindrome1(string):
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


def commonCharacters(strings):
    map = {}
    res = []
    for strg in strings:
        uniq = set(strg)
        for i in uniq:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1

    for char, count in map.items():
        if count == len(strings):
            res.append(char)
    return res


string = "abcdcaf"


def firstNonRepeatingCharacter(string):
    map = {}
    for char in string:
        # map[char] = map.get(char, 0) + 1
        if char in map:
            map[char] += 1
        else:
            map[char] = 1
    for i in range(len(string)):
        ch = string[i]
        if map[ch] == 1:
            return i
    return -1


def semordnilap(words):
    res = []
    charac = set(words)
    for char in words:
        temp = char[::-1]
        if temp in charac and temp != char:
            res.append([temp, char])
            charac.remove(char)
            charac.remove(temp)
    return res


string = "abaxyzzyxf"

# O(n^3)


def longestPalindromicSubstring1(string):
    longest = ""
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i: j + 1]
            if len(substring) > len(longest) and isPalindrome(substring):
                longest = substring
    return longest


def isPalindrome(string):
    l = 0
    r = len(string) - 1
    while l < r:
        if string[l] != string[r]:
            return False
        l += 1
        r -= 1
    return True
# O(n^2)


def longestPalindromicSubstring(string):
    currentLongest = [0, 1]
    for i in range(1, len(string)):
        odd = getLongestPalin(string, i - 1, i + 1)
        even = getLongestPalin(string, i - 1, i)
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        currentLongest = max(longest, currentLongest,
                             key=lambda x: x[1] - x[0])
    return string[currentLongest[0]: currentLongest[1]]


def getLongestPalin(string, l, r):
    while l >= 0 and r < len(string):
        if string[l] != string[r]:
            break
        l -= 1
        r += 1
    return [l + 1, r]


characters = "ste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"


def generateDocument(ch, doc):
    chMap = {}
    for char in ch:
        if char in chMap:
            chMap[char] += 1
        else:
            chMap[char] = 1
    for char in doc:
        if char not in chMap or chMap[char] == 0:
            return False
        else:
            chMap[char] -= 1

    return True


ch = "helloworldO"
doc = "hello wOrld"


def reverse_words(s):
    # Разделяем строку на слова вручную
    words = []
    word = ''
    for char in s:
        if char == ' ':
            if word:
                words.append(word)
                word = ''
        else:
            word += char
    if word:
        words.append(word)

    # Меняем слова местами
    reversed_s = ''
    for word in reversed(words):
        reversed_s += word + ' '

    return reversed_s.strip()  # Убираем лишний пробел в конце


# Пример использования
s = "Hello world this is Python"
print(reverse_words(s))  # "Python is this world Hello"
