import math
def score(x, y):
    result = 0
    z = math.sqrt((x**2 + y**2))

    if z <= 1:
        result += 10
    elif z > 1 and z <= 5:
        result += 5
    elif z > 5 and z <= 10:
        result += 1
    else:
        result += 0

    return result

