def sort(stack):
    if not stack:
        return stack
    temp = stack.pop()
    sort(stack)
    inOrder(stack, temp)
    return stack


def inOrder(stack, element):
    if not stack or stack[-1] >= element:
        stack.append(element)
    else:
        temp = stack.pop()
        inOrder(stack, element)
        stack.append(temp)


def collidingAsteroids(arr):
    stack = []
    for i in arr:
        if not stack or i > 0:
            stack.append(i)
        else:
            while stack and stack[-1] > 0:
                if abs(stack[-1]) == abs(i):
                    stack.pop()
                    break
                elif abs(stack[-1]) > abs(i):
                    break
                else:
                    stack.pop()
            else:
                stack.append(i)
    return stack


arr = [-3, 7, -8, 6, 7, -5, -7]
print(collidingAsteroids(arr))
