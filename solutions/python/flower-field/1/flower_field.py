def count_surroundings(field, row, col):
    total = 0
    total_rows = len(field)
    total_col = len(field[0])
    # First check top left
    cur_row = row - 1
    cur_col = col - 1
    if cur_row >= 0 and cur_row < total_rows and cur_col >=0 and cur_col < total_col and field[cur_row][cur_col] == '*':
        total += 1

    # Second check top
    cur_row = row - 1
    cur_col = col
    if cur_row >= 0 and cur_row < total_rows and cur_col >=0 and cur_col < total_col and field[cur_row][cur_col] == '*':
        total += 1
    # Third check top right
    cur_row = row - 1
    cur_col = col + 1
    if cur_row >= 0 and cur_row < total_rows and cur_col >=0 and cur_col < total_col and field[cur_row][cur_col] == '*':
        total += 1
    # Fourth check right
    cur_row = row
    cur_col = col + 1
    if cur_row >= 0 and cur_row < total_rows and cur_col >=0 and cur_col < total_col and field[cur_row][cur_col] == '*':
        total += 1
    # Fifth check bottom right
    cur_row = row + 1
    cur_col = col + 1
    if cur_row >= 0 and cur_row < total_rows and cur_col >=0 and cur_col < total_col and field[cur_row][cur_col] == '*':
        total += 1
    # Sixth check bottom
    cur_row = row + 1
    cur_col = col
    if cur_row >= 0 and cur_row < total_rows and cur_col >=0 and cur_col < total_col and field[cur_row][cur_col] == '*':
        total += 1
    # Seventh check bottom left
    cur_row = row + 1
    cur_col = col - 1
    if cur_row >= 0 and cur_row < total_rows and cur_col >=0 and cur_col < total_col and field[cur_row][cur_col] == '*':
        total += 1
    # Eighth check left
    cur_row = row
    cur_col = col - 1
    if cur_row >= 0 and cur_row < total_rows and cur_col >=0 and cur_col < total_col and field[cur_row][cur_col] == '*':
        total += 1
    return total

def annotate(garden):
    # Function body starts here
    field = []
    for row_str in garden:
        l = []
        for c in row_str:
            if c != '*' and c != ' ':
                raise ValueError("The board is invalid with current input.")
            l.append(c)
        field.append(l)
        if len(l) != len(field[0]):
            raise ValueError("The board is invalid with current input.")  

    results = []
    for row in range(len(field)):
        current = []
        for col in range(len(field[0])):
            cell = field[row][col]
            if cell == '*':
                current.append('*')
            elif count_surroundings(field, row, col) > 0:
                current.append(str(count_surroundings(field, row, col)))

            else:
                current.append(' ')

        current = "".join(current)
        results.append(current)

    return results

print(annotate(['* *', '   ', ' * ']))
