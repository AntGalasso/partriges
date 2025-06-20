def permutations(list):
    #base, la lunghezza della lista è uguale a 1
    # posso restituire tranquillamente l'elemento stesso sottoforma di singleton
    if len(list) == 1:
        return [list]
    if(len(list) > 1):
        result = []
        for element in list:
            first_chosen = [element]
            rest = list[:element] + list[element + 1]
            for case in permutations(rest):
                result.append(first_chosen + case)

        return result


def permutationsWithForEach(lst):
    if len(lst) == 1:
        return [lst]
    result = []
    for element in lst:
        rest = lst.copy()
        rest.remove(element)
        for case in permutationsWithForEach(rest):
            result.append([element] + case)

    return result


def combinations(n, k):
    if n == k or k == 0:
        return 1
    return combinations(n-1, k) + combinations(n-1, k-1)


print(combinations(5, 4))
"""
l = [1, 2, 3, 5, 5]

print(permutationsWithForEach(l))

"""