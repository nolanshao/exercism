def encode(plain_text):
    encoded = ""
    plain_text = plain_text.lower()
    new_string = ""
    for c in plain_text:
        if c != ' ' and c!= ',' and c != '.':
            new_string += c
    for c in new_string:
        if c.isalpha():
            char = ord(c) - 97
            rahc = chr((25 - char) + 97)
            encoded += rahc
        else:
            encoded += c
    encoded_space = ""
    for i, c in enumerate(encoded):
        if i % 5 == 0 and i > 0:
            encoded_space += ' '
        encoded_space += c
    return encoded_space

def decode(ciphered_text):
    decoded = ""
    ciphered_text.lower()
    new_string = ""
    for c in ciphered_text:
        if c != ' ':
            new_string += c
    for c in new_string:
        if c.isalpha():
            char = ord(c) - 97
            rahc = chr((25 - char) + 97)
            decoded += rahc
        else:
            decoded += c
    return decoded

print(decode('vcvix rhn'))