#Github: https://github.com/elinbua/TileTraveller
#Player starts in tile(1.1) in 3x3 grid.
#Enter direction according instruction printing on the screen (north/south/east/west).
#When moving north, 0.1 is added to current tile.
#When moving south, 0.1 is subtracted from current tile.
#When moving east, 1 is added to current tile.
#When moving west, 1 is subtracted from current tile.
#To be within range of 3x3 grid, lowest number is 1 and highest is 3.3.
#If the new title is out of range of the 3x3 grid the player will stay on same location.
#If incorrect letter or direction is entered Invalid message prints on the screen.
#The game will continue until vicory location (title(3.1)).

num = 1.1
north = 'nN'    #Valid input for north
south = 'sS'    #valid input for south
east = 'eE'     #valid input for east
west = 'wW'     #vaild input for west
High = 3.3      #highest value for 3x3 grid
Low = 1         #lowest value for grid starting from 1
route = 1       #The route implies possible directions, e.g. in route 1 north is the only possible direction
count = 0

#Where can be traveled from initial tile(1.1)
print("You can travel: (N)orth.")

while True:  
    direction_str = input("Direction: ")
    move_north = round(num + 0.1 , 1)
    move_south = round(num - 0.1, 1)   
    move_west = round(num - 1.0, 1)   
    move_east = round(num + 1.0, 1)
    if (route == 1 or route == 2 or route == 6) and direction_str in north:
        move_north
        if Low < move_north <= High:
            num = move_north
        else:
            num = num
    elif (route == 2 or route == 3 or route == 4 or route == 6) and direction_str in south:
        move_south
        if Low < move_south <= High:
            num = move_south
        else:
            num = num
    elif (route == 2 or route == 3 or route == 5) and direction_str in east:
        move_east
        if Low < move_east <= High:
            num = move_east
        else:
            num = num
    elif (route == 4 or route == 5) and direction_str in west:
        move_west
        if Low < move_west <= High:
            num = move_west
        else:
            num = num
    else:
        print("Not a valid direction!")
        continue
    
    if num == 1.1 or num == 2.1:
        route = 1
        print("You can travel: (N)orth.")
    elif num == 1.2:
        route = 2
        print("You can travel: (N)orth or (E)ast or (S)outh.")
    elif num == 1.3:
        route = 3
        print("You can travel: (E)ast or (S)outh.")
    elif num == 3.3 or num == 2.2:
        route = 4
        print("You can travel: (S)outh or (W)est.")
    elif num == 2.3: 
        route = 5
        print("You can travel: (E)ast or (W)est.")
    elif num == 3.2:
        route = 6
        print("You can travel: (N)orth or (S)outh.")
    elif num == 3.1:
        print("Victory!")
        break
    count += 1