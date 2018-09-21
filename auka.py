    if direction_str == 's' or direction_str == 'S':
        south
        if 0 < south <= 3:
            annar = south
        else:
            annar = annar
    if direction_str == 'w' or direction_str == 'W':
        west
        if 0 < west <= 3:
            fyrsti = west
        else:
            fyrsti = fyrsti
    if direction_str == 'e' or direction_str == 'E':
        east
        if 0 < east <= 3:
            fyrsti = east
        else:
            fyrsti = fyrsti

#travel_nes = print("You can travel: (N)orth or (E)ast or (S)outh.")
travel_es = print("You can travel: (E)ast or (S)outh.")
#travel_ew = print("You can travel: (E)ast or (W)est.")
#travel_sw = print("You can travel: (S)outh or (W)est.")
#travel_ns = print("You can travel: (N)orth or (S)outh.")
#travel_invalid = print("Not a valid direction!")
#end = print("Victory!")

#n/N
#s/S
#e/E
#w/W

while True:
    direction_str = input("Direction: ")
    if direction_str == 'n' or direction_str == 'N':
        north
        if Low < north <= High:
            annar = north
        else:
            annar = annar

    else:
        print("Not a valid direction!")
        direction_str = input("Direction: ")
    #print(fyrsti, annar)
    if (fyrsti == 1 or fyrsti == 2) and annar == 1:
        print("You can travel: (N)orth.")
    if fyrsti == 1 and annar == 2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
    if fyrsti == 1 and annar == 3:
        print("You can travel: (S)outh or (W)est.")
    if fyrsti == 3 and annar == 3 or fyrsti == 2 and annar == 2:
        print("You can travel: (S)outh or (W)est.")
    if fyrsti == 2 and annar == 3:
        print("You can travel: (E)ast or (W)est.")
    if fyrsti == 2 and annar == 3:
        print("You can travel: (N)orth or (S)outh.")
    print("New position:", str(fyrsti) + "," + str(annar))
    count += 1


    move_north = round(num + 0.1 , 1)
        move_south = round(num - 0.1, 1)   
        move_west = round(num - 1.0, 1)   
        move_east = round(num + 1.0, 1) 

    print("New position:", round(num,1))
    print("route:", route)