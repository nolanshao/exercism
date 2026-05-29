def rotate(text, key):

    # alpha_beta = "abcdefghijklmnopqrstuvwxyz"
    new_text = ""
    
    for i in range(0, len(text), 1):
        if text[i].isalpha():
            point = ord(text[i])
            if point >= 65 and point <= 90:
                ascii = (point + key - 65) % 26 + 65
                new_text = new_text + chr(ascii)
            elif point >= 97 and point <= 122:
                ascii = (point + key - 97) % 26 + 97
                new_text = new_text + chr(ascii)
        else:
            new_text = new_text + text[i]

    return new_text

print(rotate('a', -1))
