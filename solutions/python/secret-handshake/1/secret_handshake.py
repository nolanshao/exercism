def commands(binary_str):
    tokens = list(binary_str)
    result = []
    if tokens[0] == '1':
        if tokens[1] == '1':
            result.append('jump')
        if tokens[2] == '1':
            result.append('close your eyes')
        if tokens[3] == '1':
            result.append('double blink')
        if tokens[4] == '1':
            result.append('wink')
        return result
    else:
        if tokens[4] == '1':
            result.append('wink')
        if tokens[3] == '1':
            result.append('double blink')
        if tokens[2] == '1':
            result.append('close your eyes')
        if tokens[1] == '1':
            result.append('jump')
        return result