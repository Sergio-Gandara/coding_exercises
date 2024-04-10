

import argparse
import os


class Box:
    xSize=0
    ySize=0
    rule="none"
    def __init__(self, x, y, rule):
        self.xSize=x; self.ySize=y
        self.rule = rule
    
    def spaceChecker(self, x, y):
        if( (x+y) % 2 == 0):
            print("*", end="")
            return
        print(" ", end="")
        return

    def updateBox(self):
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

     




def main():
    xSize=0
    ySize=0
    print("Welcome to the box printer! Please introduce x and y dimensions: ")
    xSize=input()
    ySize=input()
    myBox = Box(xSize, ySize, rule="even2*");
    os.system("clear")
    myBox.updateBox()


if __name__=='__main__':
    main()