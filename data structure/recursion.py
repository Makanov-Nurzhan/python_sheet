# permutations
def getPermutations(array):
    res = []
    # base case
    if (len(array) == 1):
        return [array[:]]

    for i in range(len(array)):
        n = array.pop(0)
        perms = getPermutations(array)

        for perm in perms:
            perm.append(n)
        res.extend(perms)
        array.append(n)

    return res


def powerset(array):
    if len(array) == 0:
        return [[]]
    else:
        first = array[0]
        rest_powerset = powerset(array[1:])
        new_subsets = []
        for subset in rest_powerset:
            new_subset = [first] + subset
            new_subsets.append(new_subset)
        return rest_powerset + new_subsets


array = [1, 2, 3]
print(powerset(array))
