from window import Window 
from graphics import Cell, Line, Point

def main():
    win = Window(800, 600)
    cell = Cell(win, 100, 100, 200, 200)
    cell.draw()
    win.wait_for_close()
    
if __name__ == "__main__":
    main()