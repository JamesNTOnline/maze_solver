from tkinter import Tk, BOTH, Canvas
# remember to setup x server for gui on wsl

'''
A window object contains a canvas which can be used for drawing
'''
class Window:
    def __init__(self, width, height, title="Maze Solver"):
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.root.title(title)
        self.canvas = Canvas()
        self.canvas.pack() # must pack the canvas to make it visible
        self.running = False

    def draw_line(self, line, colour="black"):
        line.draw(self.canvas, colour)
        

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    # Tkinter is not reactive - must redraw the window to update it
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    
    def close(self):
        self.running = False
        
    def run(self):
        self.root.mainloop()