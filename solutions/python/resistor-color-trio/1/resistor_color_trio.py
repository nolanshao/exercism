def label(colors):
    colours_map = {
        'black': 0,
        'brown': 1,
        'red': 2,
        'orange': 3,
        'yellow': 4,
        'green': 5,
        'blue': 6,
        'violet': 7,
        'grey': 8,
        'white': 9}
    
    result = ""
    for i in range(2):
        result += str(colours_map[colors[i]])
    
    for i in range(colours_map[colors[2]]):
        result += '0'

    result_int = int(result)

    if result_int // (10 ** 9) > 0:
        return f"{result_int // (10 ** 9)} gigaohms"
    elif result_int // (10 ** 6) > 0:
        return f"{result_int // (10 ** 6)} megaohms"
    elif result_int // (10 ** 3) > 0:
        return f"{result_int // (10 ** 3)} kiloohms"
    else:
        return f"{result_int} ohms"
    # if len(result) < 5:
    #     if len(result) < 3:
    #         if result[-3] == '0':
    #             return f"{result[0:-3]} kiloohms"
    #     else:
    #         return f"{result} ohms"
    # else:
    #     if len(result) < 8:
    #         return f"{result[0:-3]} kiloohms"
    #     else:
    #         if len(result) < 11:
    #             return f"{result[0:-6]} megaohms"
    #         else:
    #             return f"{result[0:-9]} gigaohms"

print(label(["orange", "orange", "orange"]))