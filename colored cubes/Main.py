cubes = int(input("enter the number of cubes: "))
weight = list()
dimension = list()
colors = list()
temporary = list()
LDS = [1 for num in range(0, cubes)]
result = 0
empty = True
numbers = set()
for i in range(0, cubes):
    tmp = int(input(f"enter {i + 1}th cubes's weight : "))
    weight.append(tmp)
    x = int(input(f"{i + 1}th length : "))
    y = int(input(f"{i + 1}th width : "))
    z = int(input(f"{i + 1}th height : "))
    dimension.append((x, y, z))

    for j in range(0, 6):
        R = int(input("enter R : "))
        G = int(input("enter G : "))
        B = int(input("enter B : "))
        tup = (R, G, B)
        temporary.append(tup)

    colors.append(temporary)

for i in range(0, cubes):
    for j in range(0, i):
        if weight[j] > weight[i] and LDS[i] < LDS[j] + 1:
            LDS[i] = LDS[j] + 1
            numbers.add(weight[i])
            numbers.add(weight[j])
            if empty == True or weight[j] == min(numbers):

                if empty == True: empty = False

                for k in range(0, 6):
                    R2 = 255 - colors[i][k][0]
                    G2 = 255 - colors[i][k][0]
                    B2 = 255 - colors[i][k][0]
                    negative = (R2, G2, B2)

                    if negative in colors[j]:
                        temp = colors[j].index(negative)
                        if k < 2:
                            result += dimension[i][0]
                        elif k > 3:
                            result += dimension[i][2]
                        else:
                            result += dimension[i][1]

                        if temp < 2:
                            result += dimension[j][0]
                        elif temp > 3:
                            result += dimension[j][2]
                        else:
                            result += dimension[j][1]

                        break
                
print(f"the height of tower is : {result}")
