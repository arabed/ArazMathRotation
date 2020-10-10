from tkinter import *
import numpy as np
class MathRotation:

    # Initializing 
    def __init__(self, root, w, h):
        print('Initilization.') 
        self.w = w
        self.h = h
        self.dx = 40
        self.dy = 40
        self.oriPoints = None
        self.rotatingPolygon = None
        self.rotationText = None

        self.root = root
        root.title("Simple Rotation Lab - A.B. La Crescenta CA 2020")
        self.canvas = Canvas(self.root, width=self.w, height=self.h)
        self.canvas.pack()
        self.frame = Frame(self.root, width=self.w, height=self.h)

        self.bindEvents()
        self.drawGrid()

    # Deleting (Calling destructor) 
    def __del__(self): 
        print('Destructor called.') 

    def bindEvents(self):
        self.root.bind("<Key>", self.key)
        self.root.bind("<Motion>", self.motion)
        self.root.bind("<Button-1>", self.click)

    def drawGrid(self):
        x_offset = self.w / 2
        y_offset = self.h / 2
        x_value = -10
        y_value =  10
        for x in range(0, self.w, self.dx):
            self.canvas.create_line(x, 0, x, self.h, fill="#808080", width=1)
            self.canvas.create_line(x, y_offset - 5, x, y_offset + 5, fill="#6060FF", width=3)
            self.canvas.create_text(x + 5, 20 + self.h / 2, justify=CENTER, fill="#808080", font="Arial 12 bold", text=str(int(x_value)))
            x_value = x_value + 1
        for y in range(0, self.h, self.dy):
            self.canvas.create_line(0, y, self.w, y, fill="#808080", width=1)
            self.canvas.create_line(x_offset - 5, y, x_offset + 5, y, fill="#6060FF", width=3)
            self.canvas.create_text(20 + self.w / 2, y, justify=CENTER, fill="#808080", font="Arial 12 bold", text=str(int(y_value)))
            y_value = y_value - 1
        self.canvas.create_line(x_offset, 0, x_offset, self.h, fill="#6060FF", width=3)
        self.canvas.create_line(0, y_offset, self.w, y_offset, fill="#6060FF", width=3)
    
    def createPolygon(self, points):
        self.oriPoints = points

    def drawPolygon(self, radians, color, rotationPolygon):
        drawPoints = []
        for x,y in self.oriPoints:
            xx =  x * np.cos(radians) - y * np.sin(radians)
            yy = -x * np.sin(radians) - y * np.cos(radians)
            x = (xx * self.dx) + (self.w / 2)
            y = (yy * self.dx) + (self.h / 2)
            drawPoints.append(x)
            drawPoints.append(y)
        if rotationPolygon:
            self.rotatingPolygon = self.canvas.create_polygon(drawPoints, outline=color, fill='', width=2)
            self.rotationText = self.canvas.create_text(60, self.h - 60, justify=LEFT, fill="#8080FF", font="Arial 28 bold", text=str(int(radians * 180 / np.pi))+"\u00B0")
        else:
            self.canvas.create_polygon(drawPoints, outline=color, fill='', width=2)

    def key(self, event):
        print("pressed", repr(event.char))

    def motion(self, event):
        x = event.x - self.w / 2
        y = event.y - self.h / 2
        radians = np.arctan2(-y, x)
        self.canvas.delete(self.rotationText)
        self.canvas.delete(self.rotatingPolygon)
        self.drawPolygon(0, '#40FF80', False)
        self.drawPolygon(radians, '#FF8040', True)
        print('{}'.format(radians * 180 / np.pi))

    def click(self, event):
        self.frame.focus_set()
        print("clicked at", event.x, event.y)

if __name__ == "__main__":
    root = Tk()
    mathRotation = MathRotation(root, 800, 800)
    mathRotation.createPolygon([(0,3),(1,1),(-3,3),(3,-1)])
    mathRotation.drawPolygon(0, '#40FF80', False)
    root.mainloop()
