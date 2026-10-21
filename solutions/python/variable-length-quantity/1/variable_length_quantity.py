def encode1(number):
    bstr = f"{number:b}"
    if len(bstr) % 7 != 0:
        zcnt = 7 - (len(bstr) % 7)
        for i in range(zcnt):
            bstr = '0' + bstr

    n = len(bstr) // 7

    tokens = []
    for i in range(0, len(bstr), 7):
        tokens.append(bstr[i:i+7])

    bits = []
    for i in range(n - 1):
        bits.append(f"1{tokens[i]}")
    bits.append(f"0{tokens[-1]}")

    print(bits)
    if bits[-1][0] != '0':
        print( 'True')
        raise ValueError("incomplete sequence")
    results = []
    for s in bits:
        results.append(int(s, 2))
        print(f"{results[-1]:x}")

    return results

def encode(numbers):
    results = []
    for n in numbers:    
        results.extend(encode1(n))
    return results

def decode0(byte):
    bstr = "".join(byte)
    print(bstr)
    result = int(bstr, 2)
    return result

def decode(bytes):
    blis = []
    barr = []
    for b in bytes:
        blis.append(f"{b:08b}")
        print(f"{b:08b}")

    if blis[-1][0] != '0':
        raise ValueError("incomplete sequence")
    
    current = []
    print(blis)
    for b in blis:
        current.append(b[1:])
        print(b[0:] + " flag")
        if b[0] == '0':
            barr.append(current)
            current = []
    print(barr)
    results = []
    for sublist in barr:    
        results.append(decode0(sublist))
    return results



print(decode([0x7F]))