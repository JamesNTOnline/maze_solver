from tkinter import Tk, BOTH, Canvas
# remember to setup x server for gui on wsl
class Window:
    def __init__(self, width, height, title="Maze Solver"):
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.root.title(title)
        self.canvas = Canvas()
        self.canvas.pack()
        self.running = False

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    
    def close(self):
        self.running = False
        
    
    def run(self):
        self.root.mainloop()