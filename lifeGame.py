import os, time

SPACEWIDTH = 40
Space = []
for x in range(SPACEWIDTH):
    Space.append([])
    for y in range(SPACEWIDTH):
        Space[x].append(' ')

def getColor(x, y):
    if getNumberOfNeighbors(x,y) < 2:
        return '\033[91m'
    else:
        return '\033[96m'


def getNumberOfNeighbors(x,y):
    neighbors = 0
    for nx, ny in ([-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]):
        try:
            if Space[x + nx][y + ny] == '☺':
                neighbors +=1
        except:
            continue
    return neighbors


def updateSpace():
    newSpace = []
    for x in range(SPACEWIDTH):
        newSpace.append([])
        for y in range(SPACEWIDTH):
            if getNumberOfNeighbors(x, y) > 3 or getNumberOfNeighbors(x, y) < 2:
                newSpace[x].append(' ')
            else:
                newSpace[x].append('☺')
    return newSpace


def printSpace():
    os.system('cls')
    print('╔' + '= ' * SPACEWIDTH +'╗')
    for x in range(SPACEWIDTH):
        print('║', end='')
        for y in range(SPACEWIDTH):
            if Space[x][y] == '☺':
                print(getColor(x,y) + "☺" + '\033[0m', end=' ')
            else:
                print(' ',end=' ')
        print('║')
    print('╚' + '= ' * SPACEWIDTH + '╝')

Space[12][11] = '☺'
Space[11][11] = '☺'
Space[10][11] = '☺'
#Space[12][12] = '☺'
while True:
    printSpace()
    Space = updateSpace()
    time.sleep(3)
    smilesnum = 0
    for x in range(SPACEWIDTH):
        if not '☺' in Space[x]:
            continue
        else:
            smilesnum += 1
    if smilesnum == 0 or Space == updateSpace():
        break