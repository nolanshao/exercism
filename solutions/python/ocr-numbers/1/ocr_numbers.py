map = {
    ' _ | ||_|   ' : '0',
    '     |  |   ' : '1',
    ' _  _||_    ' : '2',
    ' _  _| _|   ' : '3',
    '   |_|  |   ' : '4',
    ' _ |_  _|   ' : '5',
    ' _ |_ |_|   ' : '6',
    ' _   |  |   ' : '7',
    ' _ |_||_|   ' : '8',
    ' _ |_| _|   ' : '9'
}


def convert(input_grid):
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if len(input_grid[0]) % 3 != 0:
        raise ValueError("Number of input columns is not a multiple of three") 
    results = ""
    for j in range(0, len(input_grid), 4):
        if j > 0:
            results += ','
        for i in range(0, len(input_grid[j]), 3):
            key = input_grid[j][i:i+3] + input_grid[j+1][i:i+3] + input_grid[j+2][i:i+3] + input_grid[j+3][i:i+3]
            if key in map:
                results += map[key]
            else:
                results += '?'
    return results

print(map[' _ | ||_|   '])


