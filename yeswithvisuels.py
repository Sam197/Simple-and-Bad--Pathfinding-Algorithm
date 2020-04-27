import random
import pygame
from pygame import *
import time

SHOW_AT_ALL = True    #For speed, doesn't have any visuals
SHOW_STEP = True      #Shows each iteration of the loops
STEP_BY_STEP = True  #Iterates over in the loop on mouse click
DRAW_OBSTICALS = True

if STEP_BY_STEP:
    SHOW_STEP = True  #These staments are here to make sure things won't crash if I'm an idiot

if SHOW_STEP:
    SHOW_AT_ALL = True

if not SHOW_AT_ALL:
    SHOW_STEP = False

if not SHOW_STEP:
    STEP_BY_STEP = False


if SHOW_AT_ALL:
    pygame.init()

#Max X = 93 Y = 47   #Can get to around 1750 obsticles

GRIDX = 50
GRIDY = 25
obsticals = 500
#obsticals = (GRIDX*GRIDY)*0.4     #Genral max amount of obsitcals in the grid
global attempts
attempts = 0
TILE_SIZE = 20
if SHOW_AT_ALL:
    FONT = pygame.font.SysFont('comicsans', 20)

global startstart
startstart = time.time()

print("Oh dear")            #First line of code written do not remove

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

def find_coords(grid, num):    #Finds the coordiates of any instance of a given int or char and returns a list of those coords
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

def bubbleSort(testList, otherList):    #Bubble sort ftw
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
            return otherList          #Vauge variable names ftw

def print_grid(grid):               #Method that prints the grid to the console, not used anymore 

    for row in grid:
        for col in row:
            print(col, end = " ")    
        print()

def show_to(grid, screen):          #Displays the grid to pygame window
    screen.fill((255,255,255))
    ycoord = 0
    for row in grid:
        xcoord = 0
        for col in row:
            if not str(col).isdigit() and col != "#" and col != "E":    #Chnages colour of objects depending on what it is
                colour = (255,0,0)                                      #Yes this logic could be a lot better
            elif str(col).isdigit() and col != 0:
                colour = (0,0,255)
            elif col == "#":
                colour = (0, 255,0)
            else:
                colour = (0,0,0)
            pygame.draw.rect(screen, (255,255,255), (xcoord, ycoord, TILE_SIZE, TILE_SIZE))
            text = FONT.render(str(col), 1, colour)
            screen.blit(text, (xcoord, ycoord))
            xcoord += TILE_SIZE
        ycoord += TILE_SIZE
    pygame.display.update()

def main():
    
    global startstart     #I hate the fact I have to delcare these as globals, there already globals
    global attempts
    attempts += 1
    if SHOW_AT_ALL:
        screen = pygame.display.set_mode(((GRIDX+2)*TILE_SIZE, (GRIDY+2)*TILE_SIZE))     #Setting the screen size, avoding magic numbers
        #screen = pygame.display.set_mode((440, 440))
        screen.fill((255,255,255))

    grid = make_grid()
    starting_grid = make_grid()
    x = 0

    if not DRAW_OBSTICALS:
        while x < obsticals:                        #Add in obsicals randomly
            gy = random.randrange(0, GRIDY + 1)
            gx = random.randrange(0, GRIDX + 1)
            if grid[gy][gx] != "#":               
                grid[gy][gx] = "#"
                starting_grid[gy][gx] = "#"
                x += 1

    #chose random start and end points
    # curX = random.randrange(1, GRIDX - 1)
    # curY = random.randrange(1, GRIDY - 1)
    # grid[curY][curX] = "S"
    # starting_grid[curY][curX] = "S"
    # Fy = random.randrange(1, GRIDY - 1)
    # Fx = random.randrange(1, GRIDX - 1)
    # grid[Fy][Fx] = "F"
    # starting_grid[Fy][Fx] = "F"
    
    #Chosing set start and end points
    curX = 2
    curY = 2
    grid[curY][curX] = "S"
    starting_grid[curY][curX] = "S"
    grid[GRIDY-2][GRIDX-2] = "F"
    starting_grid[GRIDY-2][GRIDX-2] = "F"
    
    if DRAW_OBSTICALS:
        drawing = True
        mousedown = False
        while drawing:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousedown = True
                    print(x)
                if event.type == pygame.MOUSEBUTTONUP:
                    mousedown = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        drawing = False
                if mousedown:
                    x, y = pygame.mouse.get_pos()
                    x = int(x/TILE_SIZE)
                    y = int(y/TILE_SIZE)
                    grid[y][x] = "#"
                    starting_grid[y][x] = "#"
            show_to(grid, screen)

    #print_grid(grid)
    if SHOW_AT_ALL:
        show_to(grid, screen)

    step = 0
    curSteps = 0
    coords = [(curY, curX)]
    notFound = True
    start = time.time()
    moveon = True

    while notFound:

        if STEP_BY_STEP:
            moveon = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        moveon = True

        if SHOW_AT_ALL:
            pygame.event.pump()   #This allows pygame to go through it's event magement, stops it going into no respond mode

        if moveon:
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

            if len(coords) == 0:    #If no coords returned, it is impossible
                curSteps += 1
            if curSteps > 1:
                if SHOW_AT_ALL:
                    pygame.display.set_caption("Impossible")
            if curSteps == 10:       #Resets map
                del grid
                del starting_grid
                main()
                    

            #time.sleep(0.1)
            #print_grid(grid)
            if SHOW_STEP:
                show_to(grid, screen)
            coords = find_coords(grid, step)
            if SHOW_AT_ALL:                     #Long line - ooooooooooooo
                pygame.display.set_caption(str(step) + " step" + "   " + str(attempts) + " attempts     " + "Cur Time " + str(time.time()-start) + "   " + "Total Time " + str(time.time()-startstart ))
            #print(coords)
            #print(step)
    
    for curY, curX in find_coords(grid, 0):   #E
        grid[curY][curX] = "E"

    coords = find_coords(grid, "F")
    curY, curX = coords[0]
    #print_grid(grid)
    #show_to(grid, screen)
    Not_back = True
    moveon = True

    while Not_back:
        if SHOW_AT_ALL:
            pygame.event.pump()
        numsAround = []
        otherList = []
        if STEP_BY_STEP:
            moveon = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        moveon = True

        if moveon:    
            if str(grid[curY][curX + 1]).isdigit():       #.isdigit() checks for number
                numsAround.append(grid[curY][curX + 1])
                otherList.append("Right")
            if str(grid[curY][curX + 1]) == "S":
                break
            if str(grid[curY][curX - 1]).isdigit():
                numsAround.append(grid[curY][curX - 1])
                otherList.append("Left")
            if str(grid[curY][curX - 1]) == "S":
                break
            if str(grid[curY + 1][curX]).isdigit():            
                numsAround.append(grid[curY + 1][curX])
                otherList.append("Down")
            if str(grid[curY + 1][curX]) == "S":
                break
            if str(grid[curY - 1][curX]).isdigit():
                numsAround.append(grid[curY - 1][curX])
                otherList.append("Up")
            if str(grid[curY - 1][curX]) == "S":
                break
            directions = bubbleSort(numsAround, otherList)    #Bubble sort ftw
            if directions[0] == "Right":
                curX += 1
            elif directions[0] == "Left":
                curX -= 1
            elif directions[0] == "Down":
                curY += 1
            elif directions[0] == "Up":
                curY -= 1
            
            #time.sleep(0.1)
            grid[curY][curX] = "P"
            if SHOW_STEP:
                show_to(grid, screen)

    #print_grid(grid)
    if SHOW_STEP:
        show_to(grid, screen)

    for y, x in find_coords(grid, "P"):
        #show_to(grid, screen)
        starting_grid[y][x] = "P"

    #print_grid(starting_grid)
    if SHOW_AT_ALL:
        show_to(starting_grid, screen)

    # time.sleep(1)
    # del grid
    # del starting_grid
    # main()
    a = True
    print(time.time()- start)

    if SHOW_AT_ALL:
        while a:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    a = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[2]:      #Right click to reset map
                        del grid
                        del starting_grid
                        attempts = 0
                        startstart = time.time()
                        main()

main()   #I always forget this line