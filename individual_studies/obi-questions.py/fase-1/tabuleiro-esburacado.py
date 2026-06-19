n = int(input())
moves_played = list(map(int, input().split()))

initial_position = [4,3]

dangers_cord = [[1,3], [2,3],[2,5], [5,4]]

final_positionx = 4
final_positiony = 3

stop = False
moves_done = 0

moves_deslocament = {
    1 : [1,2],
    2 : [2,1],
    3 : [2,-1],
    4 : [1, -2],
    5 : [-1, -2],
    6 : [-2, -1],
    7 : [-2, 1],
    8 : [-1, 2],
}

for num in moves_played :

    if stop :
        break
    
    if moves_done == 0 :
        final_positionx = initial_position[0] + moves_deslocament[num][0]
        final_positiony = initial_position[1] + moves_deslocament[num][1]
    else :
        final_positionx += moves_deslocament[num][0]
        final_positiony += moves_deslocament[num][1]

    for cord in dangers_cord :
        if [final_positionx, final_positiony] == cord :
            stop = True
    
    moves_done += 1



print(moves_done)

