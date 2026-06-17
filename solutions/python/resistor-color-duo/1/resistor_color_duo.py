def value(colors):
    result = ""
    colours = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    
    for i in range(0, 2, 1):
        result += str(colours.index(colors[i]))
    return int(result)

print(value(["brown", "black"]))