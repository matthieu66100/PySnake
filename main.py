from ctypes.wintypes import SIZE
from tkinter import *
from random import randint

class Const():
    SPEED = 1100 // 10
    SIZE = 20

class Game(Canvas):
    def __init__(self):

        super().__init__(
            width = 800,
            height = 800,
            background = '#333333',
            highlightthickness=0
        )
        self.pack()

    
class Serpent():
    def __init__(self):
        self.posX = 0
        self.posY = 0
        self.direction = True
    
    def draw(self):
        self.cube = Game.create_rectangle(self.posX,self.posY,self.posX+Const.SIZE,self.posY+Const.SIZE,fill='green')




ws = Tk()
ws.title('Snake')


board = Game()

ws.mainloop()