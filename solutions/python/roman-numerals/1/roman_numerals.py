def roman(number):

#     numerals = {
#         'I' : 1,
#         'IV': 4,
#         'V' : 5,
#         'IX': 9,
#         'X' : 10,
#         'XL': 40,
#         'L' : 50,
#         'XC': 90,
#         'C' : 100,
#         'CD': 400,
#         'D' : 500,
#         'CM': 900,
#         'M' : 1000
#     }

#     result = 0
#     i = 0
#     while i < len(number) - 1:
#         group_candidate = number[i : i+2]
#         if group_candidate in numerals:
#             result += numerals[group_candidate]
#             i += 2
#         else:
#             result += numerals[number[i]]
#             i += 1

#     if i == len(number):
#         return result
#     else:
#         return result + numerals[number[-1]]

# print(roman('CIV'))

    numerals = {
        1 : 'I',
        2 : 'II',
        3 : 'III',
        4 : 'IV',
        5 : 'V',
        6 : 'VI',
        7 : 'VII',
        8 : 'VIII',
        9 : 'IX',
        10 : 'X',
        20 : 'XX',
        30 : 'XXX',
        40 : 'XL',
        50 : 'L',
        60 : 'LX',
        70 : 'LXX',
        80 : 'LXXX',
        90 : 'XC',
        100 : 'C',
        200 : 'CC',
        300 : 'CCC',
        400 : 'CD',
        500 : 'D',
        600 : 'DC',
        700 : 'DCC',
        800 : 'DCCC',
        900 : 'CM',
        1000 : 'M',
        2000 : 'MM',
        3000 : 'MMM'
    }

    result = ''
    denom = 1000
    while denom > 0:
        digit = number // denom
        if digit > 0:
            result += numerals[digit * denom]
            number = number - digit * denom
        denom = denom // 10

    return result

    # result = 0
    # string = str(number)
    # num_list = list(string)
    # length = len(num_list)
    # for i in range(length):
    #     result += numerals[int("".join(num_list[length - i : length]))]
    #     num_list[length - i] = '0'

    # return result

print(roman(400))