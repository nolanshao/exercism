def score(x):
    return x[0] * 3 + x[1]

def tally(rows):
    table = ["Team                           | MP |  W |  D |  L |  P"]
    teams = {}

    for r in rows:
        game = r.split(';')
        if game[2] == 'win':
            if game[0] in teams:
                teams[game[0]][0] += 1
            else:
                teams[game[0]] = [1, 0, 0]
            if game[1] in teams:
                teams[game[1]][2] += 1
            else:
                teams[game[1]] = [0, 0, 1]
        elif game[2] == 'loss':
            if game[0] in teams:
                teams[game[0]][2] += 1
            else:
                teams[game[0]] = [0, 0, 1]   
            if game[1] in teams:
                teams[game[1]][0] += 1
            else:
                teams[game[1]] = [1, 0, 0]         
        else:
            if game[0] in teams:
                teams[game[0]][1] += 1
            else:
                teams[game[0]] = [0, 1, 0]
            if game[1] in teams:
                teams[game[1]][1] += 1
            else:
                teams[game[1]] = [0, 1, 0]

    sorted_list = []
    for key, value in teams.items():
        sorted_list.append((key, value))
    sorted_list.sort(key = lambda x: (-score(x[1]), x[0]))
    for (key, value) in sorted_list:    
        team_score = f"{key}".ljust(31) + '|'
        MP = value[0] + value[1] + value[2]
        team_score += f'{MP}'.rjust(3) + ' |'
        team_score += f'{value[0]}'.rjust(3) + ' |'
        team_score += f'{value[1]}'.rjust(3) + ' |'
        team_score += f'{value[2]}'.rjust(3) + ' |'
        team_score += f'{score(value)}'.rjust(3)

        table.append(team_score)

    for t in teams:
        print(f'{t}\t {teams[t]}')
    return(table)

print(tally([ "Courageous Californians;Devastating Donkeys;win",
            "Allegoric Alaskans;Blithering Badgers;win",
            "Devastating Donkeys;Allegoric Alaskans;loss",
            "Courageous Californians;Blithering Badgers;win",
            "Blithering Badgers;Devastating Donkeys;draw",
            "Allegoric Alaskans;Courageous Californians;draw",]))
        
        


































# """
#   O
#  /|\
# ( | \
#  / \
# /   |

#   O
#  /|
#  \|\
#   |\
#   |/

#    O
#   /|\
#  / | \
#    |\
#   /  \
# """