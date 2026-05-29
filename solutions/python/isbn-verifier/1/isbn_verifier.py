def is_valid(isbn):
    c = isbn.replace("-","")
    print(c)
    if len(c) > 10 or len(c) < 10:
        return False
    for i in range(0, 8, 1):
        if c[i].isalpha():
            return False
    
    if c[9] == "X":
        numbers = []
        for i in range(0, 9, 1):
            numbers.append( int(c[i]) * (10 - i))
        total = sum(numbers)
        total += 10
        print(numbers)
        print(total)
        if total % 11 == 0:
            return True
        else:
            return False
    # if c[9] == "X":
    #     if ((c[0] * 10) + (c[1] * 9) + (c[2] * 8) + (c[3] * 7) + (c[4] * 6) + (c[5] * 5) + (c[6] * 4) + (c[7] * 3) + (c[8] * 2) + 10) % 11 == 0:
    #         return True
    #     else:
    #         return False
    elif c[9].isalpha() == False:

        numbers = []
        for i in range(0, 10, 1):
            numbers.append(int(c[i]) * (10 - i))
            print(numbers)
        total = sum(numbers)

        if total % 11 == 0:
            return True
        else:
            return False
    else:
        return False
    # else:
    #     c = int(c)
    #     if ((c[0] * 10) + (c[1] * 9) + (c[2] * 8) + (c[3] * 7) + (c[4] * 6) + (c[5] * 5) + (c[6] * 4) + (c[7] * 3) + (c[8] * 2) + c[9]) % 11 == 0:
    #         return True
    #     else:
    #         return False

is_valid("359821507X")