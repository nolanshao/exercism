numbers = {
    1 : ('One', 'no'),
    2 : ('Two', 'one'),
    3 : ('Three', 'two'),
    4 : ('Four', 'three'),
    5 : ('Five', 'four'),
    6 : ('Six', 'five'),
    7 : ('Seven', 'six'),
    8 : ('Eight', 'seven'),
    9 : ('Nine', 'eight'),
    10: ('Ten', 'nine')
}

def recite(start, take=1):

    result = []
    for i in range(take):
        index = start - i
        if take > 1 and index < start:
            result.append("")
        if numbers[index][0] == 'One':
            result.append(f"{numbers[index][0]} green bottle hanging on the wall,")
            result.append(f"{numbers[index][0]} green bottle hanging on the wall,")
        else:
            result.append(f"{numbers[index][0]} green bottles hanging on the wall,")
            result.append(f"{numbers[index][0]} green bottles hanging on the wall,")            
        result.append("And if one green bottle should accidentally fall,")
        if numbers[index][1] == 'one':
            result.append(f"There'll be {numbers[index][1]} green bottle hanging on the wall.")
        else:
            result.append(f"There'll be {numbers[index][1]} green bottles hanging on the wall.")            

    return result

print(recite(start=2))