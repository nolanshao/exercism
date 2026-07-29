def checkwin(board_2D, coord_list, c):
    co0 = coord_list[0]
    co1 = coord_list[1]
    co2 = coord_list[2]
    return board_2D[co0[0]][co0[1]] == board_2D[co1[0]][co1[1]] == board_2D[co2[0]][co2[1]] == c


def gamestate(board):

    xcount = 0
    ocount = 0
    
    board_2D = []
    for line in board:
        line_list = []
        for c in line:
            if c == 'X':
                xcount += 1
            if c == 'O':
                ocount += 1
            line_list.append(c)
        board_2D.append(line_list)

    total = 0
    xtotal = 0
    ototal = 0
    for r in range(3):
        if checkwin(board_2D, [(r,0), (r,1), (r,2)], 'X'):
            total += 1
            xtotal += 1
        if checkwin(board_2D, [(r,0), (r,1), (r,2)], 'O'):
            total += 1
            ototal += 1
    for c in range(3):
        if checkwin(board_2D, [(0,c), (1,c), (2,c)], 'X'):
            total += 1
            xtotal += 1
        if checkwin(board_2D, [(0,c), (1,c), (2,c)], 'O'):
            total += 1
            ototal += 1

    if checkwin(board_2D, [(0,0), (1,1), (2,2)], 'X'):
            total += 1
            xtotal += 1
    if checkwin(board_2D, [(0,0), (1,1), (2,2)], 'O'):
            total += 1
            ototal += 1
    if checkwin(board_2D, [(0,2), (1,1), (2,0)], 'X'):
            total += 1
            xtotal += 1
    if checkwin(board_2D, [(0,2), (1,1), (2,0)], 'O'):
            total += 1
            ototal += 1

    print(total)

    boardfull = False
    if xcount + ocount == 9:
        boardfull = True

    #if boardfull == False:
    # invalid: wrong order
    if abs(xcount - ocount) > 1:
        raise ValueError("Wrong turn order: X went twice")
    if ocount > xcount:
        raise ValueError("Wrong turn order: O started")
    # invalid: played after win
    elif xtotal > 0 and ototal > 0:
        raise ValueError("Impossible board: game should have ended after the game was won") 
    # win
    if xtotal > 0 or ototal > 0:
        return 'win'
    # in progress
    else:
        if boardfull:
             return 'draw'
        return 'ongoing'

    
    

        # # invalid: wrong order
        # if abs(xcount - ocount) > 1:
        #     raise ValueError("Wrong turn order: X went twice")
        # if ocount > xcount:
        #     raise ValueError("Wrong turn order: O started")
        # # invalid: played after win
        # elif xtotal > 0 and ototal > 0:
        #     raise ValueError("Impossible board: game should have ended after the game was won") 
        # # win
        # if total == 1:
        #     return 'win'
        # # in progress
        # else:
        #     return 'draw'
        # # win

print(gamestate(
           ["XXX",
            "XOO",
            "XOO",]
            ))