def is_armstrong_number(number):
    tokens = str(number)
    l = len(tokens)
    print(l)

    armstrong = []
    for i in range(0,l,1):
        num = int(tokens[i])
        print(num)
        armstrong.append(num**l)
    print(armstrong)
    result = sum(armstrong)

    print(result)
    if result == number:
        return True
    else:
        return False

is_armstrong_number(153)