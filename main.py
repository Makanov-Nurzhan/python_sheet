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


dict = my_dict = {'b': 3, 'a': 1, 'c': 2, 'd': 2}

print(sorted(dict.items(), key=lambda item: (-item[1], item[0])))
