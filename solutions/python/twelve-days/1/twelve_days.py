def verse(number):

    start_dict = {
        1: 'first',
        2: 'second',
        3: 'third',
        4: 'fourth',
        5: 'fifth',
        6: 'sixth',
        7: 'seventh',
        8: 'eighth',
        9: 'ninth',
        10: 'tenth',
        11: 'eleventh',
        12: 'twelfth'
        }
    
    end_dict = {
        1: 'and a Partridge in a Pear Tree.',
        2: 'two Turtle Doves, ',
        3: 'three French Hens, ',
        4: 'four Calling Birds, ',
        5: 'five Gold Rings, ',
        6: 'six Geese-a-Laying, ',
        7: 'seven Swans-a-Swimming, ',
        8: 'eight Maids-a-Milking, ',
        9: 'nine Ladies Dancing, ',
        10: 'ten Lords-a-Leaping, ',
        11: 'eleven Pipers Piping, ',
        12: 'twelve Drummers Drumming, '
        }

    results = []
    start = start_dict[number]
    result = f"On the {start} day of Christmas my true love gave to me: "
    results.append(result)

    for i in range(number):
        if number == 1:
            results.append('a Partridge in a Pear Tree.')
        else:
            results.append(end_dict[number - i])

    result_str = "".join(results)
    return result_str

def recite(start_verse, end_verse):

    result = []
    s = start_verse
    e = end_verse

    for i in range(s, e + 1):
        result.append(verse(i))

    return result


print(recite(1, 3))
