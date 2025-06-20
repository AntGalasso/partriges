def solution(words, group):
    result = list()
    last_equal = group[0]
    result.append(words[0])
    for i in range(1, len(words)):
        if group[i] != last_equal:
            last = group[i]
            result.append(words[i])

    return result

word = ['e', 'a', 'r']
group = [0, 0, 1]

print(solution(word, group))




