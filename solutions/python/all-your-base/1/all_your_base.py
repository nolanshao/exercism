def base10(input_base, digits):
    result = 0
    n = len(digits)
    for i in range(n):
        result += digits[i] * input_base ** (n-i-1)
    return result

def countdigits(result, output_base):
    digit = 0
    while result // output_base > 0:
        result //= output_base
        digit += 1
    return digit + 1

def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    for d in digits:
        if d < 0 or d >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    result = base10(input_base, digits)
    num_digits = countdigits(result, output_base)
    print(result)
    print(num_digits)
    value = []
    for exponent in range(num_digits - 1, -1, -1):
        value.append(result // (output_base ** exponent))
        result -= (output_base ** exponent) * value[-1]
    return value

print(rebase(2, [], 10))