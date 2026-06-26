def rows(letter):
    
    n = ord(letter)
    n -= 64
    total_len = n * 2 - 1

    superl = []
    for i in range(n):
        l = []
        for j in range(n * 2 - 1):
            l.append(' ')

        if i == 0:
            l[n - 1] = 'A'
        else:
            l[n - (i + 1)] = chr(65 + i)
            l[-(n - i)] = chr(65 + i)
        superl.append("".join(l))
    
    for i in range((n - 2), -1, -1):
        superl.append(superl[i])
    return superl

rows('F')