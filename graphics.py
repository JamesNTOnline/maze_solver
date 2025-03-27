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
    def __init__(self, top_x, top_y, bot_x, bot_y, window=None):
        # which walls the cell has, by default it has them all
        self.top = True
        self.right = True
        self.bottom = True
        self.left = True
        # the corners of the cell
        self.tl = Point(top_x, top_y)
        self.tr = Point(bot_x, top_y)
        self.bl = Point(top_x, bot_y)
        self.br = Point(bot_x, bot_y)
        # the walls of the cell
        # tuple contains whether the wall exists and the line to draw it
        self.walls = [
            (self.top, Line(self.tl, self.tr)),
            (self.right, Line(self.tr, self.br)),
            (self.bottom, Line(self.br, self.bl)),
            (self.left, Line(self.bl, self.tl))
        ]
        # other information about the cell
        self.width = bot_x - top_x
        self.height = bot_y - top_y
        self.mid_point = Point(top_x + self.width // 2, top_y + self.height // 2)
        self.window = window
        
    def draw(self):
        if self.window is None:
            return # don't bother if there's no window to draw on
        for wall_present, line in self.walls:
            line_color = "black" if wall_present else "white"
            self.window.draw_line(line, line_color)

    def draw_move(self, to, undo=False):
        colour = "lime green" if not undo else "grey"
        # https://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html
        #origin_point = Point(self.tl.x + self.width // 2, self.tl.y + self.height // 2)
        #dest_point = Point(to.tl.x + to.width // 2, to.tl.y + to.height // 2)
        if self.mid_point == to.mid_point:
            return # don't bother if the points are the same
        self.window.draw_line(Line(self.mid_point, to.mid_point), colour)
    
'''
A line is defined by two point objects which can 
be used to draw a line on a canvas.
'''
class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

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