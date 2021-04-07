cubes = int(input("enter the number of cubes: "))
weight = list()
dimension = list()
colors = list()
temporary = list()
final_result = 0

for i in range(0, cubes):
    tmp = int(input(f"enter {i+1}th cubes's weight: "))
    weight.append(tmp)
    x = int(input(f"{i+1}th length: "))
    y = int(input(f"{i+1}th width: "))
    z = int(input(f"{i+1}th height: "))
    dimension.append((x, y, z))

    for j in range(0, 6):
        R = int(input("enter R: "))
        G = int(input("enter G: "))
        B = int(input("enter B: "))
        tup = (R, G, B)
        temporary.append(tup)

    colors.append(temporary)






