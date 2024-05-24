def inOrder(stack, element):
    if not stack or stack[-1] >= element:
        stack.append(element)
    else:
        temp = stack.pop()
        inOrder(stack, element)
        stack.append(temp)


def sort(stack):
    if stack:
        temp = stack.pop()
        sort(stack)
        inOrder(stack, temp)
    else:
        return


stack = [5, 2, 9, 1, 3]
sort(stack)
print("Отсортированный стек:", stack)
