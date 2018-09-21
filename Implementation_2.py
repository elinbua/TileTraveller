#Github: https://github.com/elinbua/TileTraveller

def start_point():
    """The game starts in num= 1.1 and possible direction is north (route = 1)"""
    num = 1.1
    route = 1
    print("You can travel: (N)orth.")
    return num, route
def direction():
    """Enter direction"""
    direction_str = input("Direction: ")
    return direction_str

def move(num, direction_str, route, Low = 1, High = 3.3):
    """Move player to next position in selected direction. The player can only
    be moved to direction in valid route.""" 
    north = 'nN'    
    south = 'sS'   
    east = 'eE'
    west = 'wW'
    valid = 1  
    if (route == 1 or route == 2 or route == 6) and direction_str in north:
        move_north = round(num + 0.1 , 1)
        if Low < move_north <= High:
            num = move_north
        else:
            num = num
    elif (route == 2 or route == 3 or route == 4 or route == 6) and direction_str in south:
        move_south = round(num - 0.1, 1)
        if Low < move_south <= High:
            num = move_south
        else:
            num = num
    elif (route == 2 or route == 3 or route == 5) and direction_str in east:
        move_east = round(num + 1.0, 1)
        if Low < move_east <= High:
            num = move_east
        else:
            num = num
    elif (route == 4 or route == 5) and direction_str in west:
        move_west = round(num - 1.0, 1) 
        if Low < move_west <= High:
            num = move_west
        else:
            num = num
    else:
        valid = 0
        print("Not a valid direction!")
    return num, valid

def new_route(num):
    """Where can player travel from current position"""
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
    return route

count = 0
end = 3.1
valid = 1
num, route = start_point()
while True:  
    direction_str = direction()
    num, valid = move(num, direction_str, route)
    if valid == 0:
        continue
    else:
        route = new_route(num)
    if num == end:
        break
    count +=1