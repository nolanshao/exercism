def is_isogram(string):
    alpha_string = ""
    for i in range(0,len(string), 1):
        if string[i].isalpha():
            alpha_string = alpha_string + string[i]
            alpha_string = alpha_string.upper()
    new_string = ""
    isogram = True
    for i in range(0, len(alpha_string), 1):
        if alpha_string[i] in new_string:
            isogram = False
        elif alpha_string[i] not in new_string:
            new_string = new_string + alpha_string[i]
        
    if isogram:
        return True
    else:
        return False

is_isogram("six-year-old")