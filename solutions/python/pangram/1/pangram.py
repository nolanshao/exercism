def is_pangram(sentence):
    all_alpha = False
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    beta = ''
    cap_sentence = sentence.upper()
    for i in range(0, len(alpha), 1):
        if alpha[i] in cap_sentence:
            beta += alpha[i]
    if alpha == beta:
        all_alpha = True

        return True
    else:
        return False

