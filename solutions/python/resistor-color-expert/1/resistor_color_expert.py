colours = {
    'black' : 0,
    'brown' : 1,
    'red' : 2,
    'orange' : 3,
    'yellow' : 4,
    'green' : 5,
    'blue' : 6,
    'violet' : 7,
    'grey' : 8,
    'white' : 9
}

tolerance = {
    'grey' : ' ±0.05%',
    'violet' : ' ±0.1%',
    'blue' : ' ±0.25%',
    'green' : ' ±0.5%',
    'brown' : ' ±1%',
    'red' : ' ±2%',
    'gold' : ' ±5%',
    'silver' : ' ±10%',
}

def resistor_label(colors):

# Band_1
    def value(index):
        return colours[colors[index]]
    ohms = ''

# Band_1.5
    if len(colors) == 1:
        ohms += str(value(0))

# Band_2
    elif len(colors) == 4:
        ohms += str(value(0))
        ohms += str(value(1))
        for i in range(value(2)):
            ohms += '0'
# Band_3
    else:
        ohms += str(value(0))
        ohms += str(value(1))
        ohms += str(value(2))
        for i in range(value(3)):
            ohms += '0'

# Band_4
    multiplier = int(ohms)

    # if len(colors) == 4:
    if len(ohms) > 6:
        if multiplier % 1000000 > 1:
            multiplier /= 1000000
        else:
            multiplier //= 1000000
        ohms = str(multiplier) + ' megaohms'
    elif len(ohms) > 3:
        if multiplier % 1000 > 1:
            multiplier /= 1000
        else:
            multiplier //= 1000
        ohms = str(multiplier) + ' kiloohms'
    else:
        ohms = str(multiplier) + ' ohms'

    # else:
    #     if len(ohms) > 6:
    #         multiplier /= 1000000
    #         ohms = str(multiplier) + ' megaohms'
    #     elif len(ohms) > 3:
    #         multiplier /= 1000
    #         ohms = str(multiplier) + ' kiloohms'
    #     else:
    #         ohms = str(multiplier) + ' ohms'        

# Band_5
    if len(colors) > 1:
        resistor = ''
        resistor += ohms
        resistor += tolerance[colors[-1]]
    else:
        resistor = ohms

    return resistor

print(resistor_label(["black"]))