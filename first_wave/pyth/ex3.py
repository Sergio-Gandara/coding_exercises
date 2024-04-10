

import os
from threading import Thread
import time



class Box:
    xSize=0
    ySize=0
    rule="none"
    enityList=[]
    def __init__(self, x, y, entityList):
        self.enityList=entityList
        self.xSize=x; self.ySize=y

    
    def spaceChecker(self, x, y): # REMOD
        try:
            for entity in self.entityList:
                print(entity.getPosition())
                if entity.getPosition() == (x, y):
                    print(entity.getBody(), end="")
        except Exception:
            print(" ", end="")
        print(" ", end="")

    def updateBox(self):
        os.system("clear")
        for i in range(int(self.ySize)):
            if i==0 or i==int(self.ySize)-1:
                for k in range(int(self.xSize)):
                    print("_", end="")
                print("")
                continue
            for j in range(int(self.xSize)):
                if j==0 or j==int(self.xSize)-1:
                    print("|", end="")
                    if j==int(self.xSize)-1:
                        print("")
                    continue
                else:
                    self.spaceChecker(i, j)


class Player:
    xPosition=0
    yPosition=0
    player_body="*"
    def __init__(self, x=1, y=1):
        self.xPosition=x; self.yPosition=y
    def move(self, xMove=0, yMove=0):
        key=input()
        horMove=0
        verMove=0
        if key=='w':
            verMove+=1
        elif key=='s':
            verMove-=1
        elif key=='a':
            horMove-=1
        elif key=='d':
            horMove+=1

        self.xPosition+=horMove; self.yPosition+=verMove

        print(self.getPosition())
        
    def getPosition(self):
        return (self.xPosition, self.yPosition)
    def getBody(self):
        return self.player_body


def gameLoop(player, myBox, fps):
    while True:
        time.sleep(1)
        myBox.updateBox()
        player.move()
        print("Player Position: {}".format(player.getPosition()))
        #print("Player Global Position: {}, {}".format(globalxMove, globalyMove))





def main():
    xSize=0
    ySize=0
    fps=20
    print("Welcome to the box printer! Please introduce x and y dimensions: ")
    xSize=input()
    ySize=input()

    player=Player(2, 2)
    entityList=[]
    entityList.append(player)
    myBox = Box(xSize, ySize, entityList)
    
    gameThread=Thread(target=gameLoop, args=(player, myBox, fps)).start()
    
    



if __name__=='__main__':
    main()