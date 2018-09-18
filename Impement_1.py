#Enter new location - n/N
#




fyrsti = 1
annar = 1
north = annar + 1
south = annar - 1
west = fyrsti - 1
east = fyrsti + 1
High = 3
Low = 1
count = 0
print_1 = 

travel_str = input("You can travel: (N)orth.")


#n/N
#s/S
#e/E
#w/W

while True:
    if travel_str == 'n' or travel_str == 'N':
        north
        if 0 < north <= 3:
            annar = north
        else:
            annar
        travel_str = input("You can travel: (N)orth or (E)ast or (S)outh.")
        #print(fyrsti, north)
    #if travel_str == 's' or travel_str == 'S':
     #   south
        #print(fyrsti, south)
    #if travel_str == 'w' or travel_str == 'W':
    #    west
        #print(west, annar)
    #if travel_str == 'e' or travel_str == 'E':
    #    east
    else:
        print("Not a valid direction!")
    print(fyrsti, annar)
    
    count += 1