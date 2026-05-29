def appropriate(sides):
    if sides[0] + sides[1] >= sides[2] and sides[0] + sides[2] >= sides[1] and sides[1] + sides[2] >= sides[0]:
        return True
    else:
        return False

def equilateral(sides):
    if appropriate(sides) == True:
        if sides[0] == sides[1] == sides[2] and sides[0] > 0:
            return True
        else:
            return False
    else:
        return False


def isosceles(sides):
    if appropriate(sides) == True:
        if sides[0] == sides[1]:
            return True
        elif sides[0] == sides[2]:
            return True
        elif sides[1] == sides[2]:
            return True
        else:
            return False
    else: 
        return False

def scalene(sides):
    if appropriate(sides) == True:
        if sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]:
            return True
        else:
            return False
    else:
        return False

print(isosceles([1,1,3]))
