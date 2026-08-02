new_dict = {')':'(', ']':'[', '}':'{'}
def is_paired(input_string):
    brackets = "([{)]}"
    new_string = ""
    for c in input_string:
        if c in brackets:
            new_string += c
    stack = []
    for c in new_string:
        if c == '(' or c == '[' or c == '{':
            stack.append(c)
        else:
            if stack == []:
                    return False
            if new_dict[c] == stack[-1]:
                stack.pop()
            else:
                return False
    return stack == []