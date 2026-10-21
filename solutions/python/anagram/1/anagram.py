def alphabetise(word):
    list = []
    for i in range(len(word)):
        list.append(word[i].lower())
    list.sort()
    sorted = "".join(list)
    return sorted


def find_anagrams(word, candidates):
    result = []
    origin = alphabetise(word)
    for i in range(len(candidates)):
        input = alphabetise(candidates[i])
        if word.lower() == candidates[i].lower():
            continue
        print(origin, input)
        if origin.lower() == input.lower():
            print("TRUE")
            result.append(candidates[i])
    return result


print(find_anagrams("Orchestra", ["cashregister", "Carthorse", "radishes"]))
    # results = []
    # counter = 0
    # tokens = list(word)
    # for i in range(tokens):
    #     if len(word) == len(candidates[i]):
    #         for i in range(tokens):
    #             if tokens[i] in candidates[i]:
    #                 counter += 1
    #             results.append(candidates)
        