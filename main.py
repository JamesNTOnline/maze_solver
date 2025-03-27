from window import Window 
from maze import Maze

def main():
    rows = 12 # maze cell count
    cols = 16
    margin = 50 # starting x/y position of maze
    screen_x = 800 # window dimensions
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / cols
    cell_size_y = (screen_y - 2 * margin) / rows
    
    window = Window(screen_x, screen_y)
    maze = Maze(margin, margin, rows, cols, cell_size_x, cell_size_y, window)
    maze._make_entrance_exit()
    
    window.wait_for_close()
    
if __name__ == "__main__":
    main()