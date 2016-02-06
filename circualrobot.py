dir = 'N'
compass = ['N','W','S','E']
lmoves = []
def direction(nextdir):
    if nextdir in ['L','R']:
        if nextdir == 'L':

            return compass[compass.index(dir) + 1 % 3]
        elif nextdir == 'R':
            return compass[compass.index(dir) - 1]
    return None

def get_new_coordinate(current):

    if dir == 'N':
        return (current[0],current[1]+1)
    elif dir == 'S':
        return (current[0],current[1]-1)
    elif dir == 'W':
        return (current[0]-1,current[1])
    elif dir == 'E':
        return (current[0]+1,current[1])

moves = "GLLG"
l = list(moves)
start_position  = (0,0)
lmoves.append(start_position)
for x in l:
    if x == 'G':
        lmoves.append(get_new_coordinate(lmoves[-1]))
    else:
        dir = direction(x)


if lmoves[0] == lmoves[-1]:
    print ("Circular")
print (lmoves)
