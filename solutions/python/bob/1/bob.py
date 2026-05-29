def response(hey_bob):
    no_alpha = True
    for c in hey_bob:
        if c.isalpha():
            no_alpha = False
            break




    if hey_bob.strip(' \t\n\r') == '':
        return 'Fine. Be that way!'
    elif hey_bob == hey_bob.upper() and '?' in hey_bob and no_alpha == False:
        return "Calm down, I know what I'm doing!"
    elif hey_bob.strip(' ')[-1] == '?':
        return 'Sure.'
    elif hey_bob == hey_bob.upper() and no_alpha == False:
        return 'Whoa, chill out!'
    else:
        return 'Whatever.'