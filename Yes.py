import random

GRIDX = 50
GRIDY = 50

print("Oh dear")

def make_grid():
    grid = []
    placeholder = []
    for x in range(GRIDX + 2):
        placeholder.append("#")
    grid.append(placeholder)
    del placeholder
    for row in range(GRIDY):
        placeholder = []
        placeholder.append("#")
        for col in range(GRIDX):
            placeholder.append(0)
        placeholder.append("#")
        grid.append(placeholder)
        del placeholder
        placeholder = []
    for x in range(GRIDX + 2):
        placeholder.append("#")
    grid.append(placeholder)
    return grid

def find_coords(grid, num):
    Ycoord = 0
    coords = []
    for row in grid:
        Xcoord = 0
        for col in row:
            if col == num:
                coords.append((Ycoord, Xcoord))
            Xcoord += 1
        Ycoord += 1
    return coords

def bubbleSort(testList, otherList):
    while True:
        through = True
        for x in range(0,len(testList)-1):
            cur = testList[x]
            curNext = testList[x+1]
            cur2 = otherList[x]
            curNext2 = otherList[x+1]
            if cur>curNext:
                testList[x] = curNext
                testList[x+1] = cur
                otherList[x] = curNext2
                otherList[x+1] = cur2
                through = False
        #print(testList)
        if through == True:
            return otherList

def print_grid(grid):

    for row in grid:
        for col in row:
            print(col, end = " ")
        print()

def main():
    grid = make_grid()
    starting_grid = make_grid()

    for x in range(100):
        gy = random.randint(1, GRIDY - 1)
        gx = random.randint(1, GRIDX - 1)
        grid[gy][gx] = "#"
        starting_grid[gy][gx] = "#"

    #chose random start and end points
    curX = random.randint(1, GRIDX - 1)
    curY = random.randint(1, GRIDY - 1)
    grid[curY][curX] = "S"
    starting_grid[curY][curX] = "S"
    Fy = random.randint(1, GRIDY - 1)
    Fx = random.randint(1, GRIDX - 1)
    grid[Fy][Fx] = "F"
    starting_grid[Fy][Fx] = "F"
    print_grid(grid)

    step = 0
    coords = [(curY, curX)]
    notFound = True

    while notFound:
        step += 1
        for curY, curX in coords:
            if grid[curY][curX + 1] == 0:
                grid[curY][curX + 1] = step
            if grid[curY][curX - 1] == 0:
                grid[curY][curX - 1] = step
            if grid[curY + 1][curX] == 0:
                grid[curY + 1][curX] = step
            if grid[curY - 1][curX] == 0:
                grid[curY - 1][curX] = step
            if grid[curY][curX + 1] == "F":
                notFound = False
            if grid[curY][curX - 1] == "F":
                notFound = False
            if grid[curY + 1][curX] == "F":
                notFound = False
            if grid[curY - 1][curX] == "F":
                notFound = False

        if step > GRIDX*GRIDY:
            while True:
                a = input("Impossible")

        print_grid(grid)
        coords = find_coords(grid, step)
        print(coords)
    
    for curY, curX in find_coords(grid, 0):
        grid[curY][curX] = step + 10

    coords = find_coords(grid, "F")
    curY, curX = coords[0]
    print_grid(grid)
    Not_back = True

    while Not_back:
        numsAround = []
        otherList = []
        if str(grid[curY][curX + 1]).isdigit():
            numsAround.append(grid[curY][curX + 1])
            otherList.append("Right")
        if str(grid[curY][curX + 1]) == "S":
            lastMove = "Right"
            break
        if str(grid[curY][curX - 1]).isdigit():
            numsAround.append(grid[curY][curX - 1])
            otherList.append("Left")
        if str(grid[curY][curX - 1]) == "S":
            lastMove = "Left"
            break
        if str(grid[curY + 1][curX]).isdigit():            
            numsAround.append(grid[curY + 1][curX])
            otherList.append("Down")
        if str(grid[curY + 1][curX]) == "S":
            lastMove = "Down"
            break
        if str(grid[curY - 1][curX]).isdigit():
            numsAround.append(grid[curY - 1][curX])
            otherList.append("Up")
        if str(grid[curY - 1][curX]) == "S":
            lastMove = "Up"
            break
        directions = bubbleSort(numsAround, otherList)
        if directions[0] == "Right":
            curX += 1
        elif directions[0] == "Left":
            curX -= 1
        elif directions[0] == "Down":
            curY += 1
        elif directions[0] == "Up":
            curY -= 1
        
        grid[curY][curX] = "P"

    print_grid(grid)

    for y, x in find_coords(grid, "P"):
        starting_grid[y][x] = "P"

    print_grid(starting_grid)




main()