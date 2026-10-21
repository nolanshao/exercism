def egg_count(display_value):
    binary_string = f"{display_value:b}"
    total = 0
    for c in binary_string:
        if c == '1':
            total += 1

    return total