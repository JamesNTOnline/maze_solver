from tkinter import Canvas
# contains all the code related to drawing the simple objects that
# will be used to represent the maze

'''
A cell object represents a cell in a maze. It has four walls
which can be set to True or False to represent whether the wall
is present or not.
the top left and bottom right corners are given by x and y
'''
class Cell:
    def __init__(self, window, top_x, top_y, bot_x, bot_y):
        # which walls the cell has, by default it has them all
        self.top = True
        self.right = True
        self.bottom = True
        self.left = True
        self.tl = Point(top_x, top_y)
        self.br = Point(bot_x, bot_y)
        # other information about the cell
        self.width = bot_x - top_x
        self.height = bot_y - top_y
        self.window = window
        
    def draw(self):
        if self.top:
            self.window.draw_line(Line(self.tl.x, self.tl.y, self.br.x, self.tl.y))
        if self.right:
            self.window.draw_line(Line(self.br.x, self.tl.y, self.br.x, self.br.y))
        if self.bottom:
            self.window.draw_line(Line(self.tl.x, self.br.y, self.br.x, self.br.y))
        if self.left:
            self.window.draw_line(Line(self.tl.x, self.tl.y, self.tl.x, self.br.y))


    def draw_move(self, to, undo=False):
        colour = "gray"
        if not undo:
            colour = "red"
        centre
    
    
'''
A line is defined by two point objects which can 
be used to draw a line on a canvas.
'''
class Line:
    def __init__(self, p1_x, p1_y, p2_x, p2_y):
        self.p1 = Point(p1_x, p1_y)
        self.p2 = Point(p2_x, p2_y)

    def draw(self, canvas, colour="black"):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=colour)

    def __eq__(self, other):
        return self.p1 == other.p1 and self.p2 == other.p2 \
            or self.p1 == other.p2 and self.p2 == other.p1
    
    
'''
A Point object represents a point in 2D space
given by its x and y coordinate
'''
class Point: # inner class used to make lines
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y