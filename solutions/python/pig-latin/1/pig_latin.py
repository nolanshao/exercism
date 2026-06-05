def translate(text):
    words = text.split(' ')
    results = []
    for word in words:
        results.append(translate_word(word))
    return " ".join(results)

def translate_word(text):
    if text[0] in "aeiou" or text[0:2] in "xr yt":
        text = text + "ay"
        return text
    
    if "qu" in text:
        counter = text.index("qu") + 2
        all_consonants = True
        for i in range(0, counter - 2, 1):
            if text[i] in "aeiou":
                all_consonants = False
                break
        if all_consonants:    
            return f"{text[counter:]}{text[0: counter]}ay"
            # text = text + (text[0:counter])
            # new_text = text[counter:len(text)]
            # new_text = new_text + "ay"
            # return new_text
        
    if "y" in text and text.index("y") > 0:
        counter = text.index("y")
        all_consonants = True
        for i in range(0, counter, 1):
            if text[i] in "aeiou":
                all_consonants = False
                break
        if all_consonants:
            return f"{text[counter:]}{text[0:counter]}ay"

            # text = text + (text[0:counter])
            # new_text = text[counter:len(text)]
            # new_text = new_text + "ay"
            # return new_text
        
    if text[0] not in "aeiou":
        counter = 0
        while text[counter] not in "aeiou":
            counter += 1
        text = text + (text[0:counter])
        new_text = text[counter:len(text)]
        new_text = new_text + "ay"
        return new_text


    
# def debug1(text):

#     counter = 0
#     while text[counter] not in "aeiou":
#         counter += 1
    
#     print(counter)
#     text = text + (text[0:counter])
#     new_text = text[counter:len(text)]
#     new_text = new_text + "ay"
#     return new_text
    
# print(debug1("therapy"))