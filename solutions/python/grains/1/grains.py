def square(number):
    if number < 65 and number > 0:
        return 2 ** (number - 1)
    else:
        raise ValueError("square must be between 1 and 64")

def total():
    totall = 0
    for i in range(1, 65, 1):
        totall += square(i)
    return totall

