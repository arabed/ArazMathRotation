from tkinter import *

class MathRotation:

    # Initializing 
    def __init__(self, root, w, h):
        print('Initilization.') 
        self.w = w
        self.h = h
        self.dx = 40
        self.dy = 40
        self.oriPoints = []

        self.root = root
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
        for x in range(0, self.w, self.dx):
            self.canvas.create_line(x, 0, x, self.h, fill="#808080", width=1)
        for y in range(0, self.h, self.dy):
            self.canvas.create_line(0, y, self.w, y, fill="#808080", width=1)
        self.canvas.create_line(x_offset, 0, x_offset, self.h, fill="#6060FF", width=3)
        self.canvas.create_line(0, y_offset, self.w, y_offset, fill="#6060FF", width=3)

        #self.canvas.create_rectangle(50, 20, 150, 80, fill="#476042")
        #self.canvas.create_rectangle(50, 20, 150, 80, fill="#476042")
        #self.canvas.create_rectangle(65, 35, 135, 65, fill="yellow")
        #self.canvas.create_line(0, 0, 50, 20, fill="#476042", width=3)
        #self.canvas.create_line(0, 100, 50, 80, fill="#476042", width=3)
        #self.canvas.create_line(150,20, 200, 0, fill="#476042", width=3)
        #self.canvas.create_line(150, 80, 200, 100, fill="#476042", width=3)
    
    def createPolygon(self, points):
        self.oriPoints.clear()
        alt = True
        for point in points:
            if alt:
                # this is x
                self.oriPoints.append((point * self.dx) + (self.w / 2))
                alt = False
            else:
                # this is y
                self.oriPoints.append((point * self.dy * -1) + (self.h / 2))
                alt = True
        self.canvas.create_polygon(self.oriPoints, outline='#008080', fill='', width=2)

    def key(self, event):
        print("pressed", repr(event.char))

    def motion(self, event):
        x, y = event.x, event.y
        print('{}, {}'.format(x, y))

    def click(self, event):
        self.frame.focus_set()
        print("clicked at", event.x, event.y)

if __name__ == "__main__":
    root = Tk()
    mathRotation = MathRotation(root, 800, 800)
    mathRotation.createPolygon([0,0,1,1,-1,1])
    root.mainloop()
