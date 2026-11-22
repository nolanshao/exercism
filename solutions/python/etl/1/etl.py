alphabet = {
    1 : ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    2 : ["D", "G"],
    3 : ["B", "C", "M", "P"],
    4 : ["F", "H", "V", "W", "Y"],
    5 : ["K"],
    8 : ["J", "X"],
    10: ["Q", "Z"],
}

def transform(legacy_data):
    result = {}
    legacy_data
    for integer, value in legacy_data.items():
        for v in value:
            result[v.lower()] = integer

    return result

