    
def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    p = 0
    for i in range(1, number, 1):
        if number % i == 0:
            p += i

    # Abundant = False
    # a = []
    # for i in range(1, number, 1):
    #     if number % i == 0:
    #         a.append(i)

    # if sum(a) == number:
    #     Abundant = True

    # Deficient = False
    # d = []
    # for i in range(1, number, 1):
    #     if number % i == 0:
    #         d.append(i)

    # if sum(d) == number:
    #     Deficient = True

    if p == number:
        return 'perfect'
    elif p > number:
        return 'abundant'
    else:
        return 'deficient'
