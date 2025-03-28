from graphics import Cell
import time
import random

'''
Maze is made up of cells, each cell is a square with four walls
which can be set to True or False to represent whether the wall
is present or not.
The maze is made up of rows and columns of cells, each cell has a
width and height.
'''
class Maze:
    '''
    window: the window object to draw the maze on
    m_x: x pos of maze origin
    m_y: y pos of maze origin
    rows: number of rows in the maze
    cols: number of columns in the maze
    cell_size_x: width of each cell
    cell_size_y: height of each cell
    '''
    def __init__(self, m_x, m_y, rows, cols, cell_size_x, cell_size_y, window=None, seed=None):
        self._m_x = m_x # x pos of maze origin
        self.m_y = m_y # y pos of maze origin
        self.rows = rows
        self.cols = cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._cells = []
        self._window = window
        if not seed == None:
            self.seed = random.seed(seed)
        self._create_cells()
    
    '''
    Populates the cell list, and then draws them all on the canvas
    '''
    def _create_cells(self):
        for i in range(0, self.cols):
            column = []
            for j in range(0, self.rows):
                cell_left = self._m_x + i * self.cell_size_x
                cell_right = cell_left + self.cell_size_x
                cell_top = self.m_y + j * self.cell_size_y
                cell_bottom = cell_top + self.cell_size_y
                cell = Cell(cell_left, cell_top, cell_right, cell_bottom, self._window)
                column.append(cell)
            self._cells.append(column)
        # Then draw them all
        for i in range(0, self.cols):
            for j in range(0, self.rows):
                self._draw_cell(i, j)
        
    def _make_entrance_exit(self):
        self._cells[0][0].open_wall("top")
        self._cells[self.cols-1][self.rows-1].open_wall("bottom")
        self._draw_cell(0, 0)
        self._draw_cell(self.cols-1, self.rows-1)
    
    def _break_walls(self, i, j):
        self._cells[i][j].visited = True
        while True:
            neighbours = []
            if i > 0 and not self._cells[i-1][j].visited:
                neighbours.append((i-1, j))
            if i < self.cols - 1 and not self._cells[i+1][j].visited:
                neighbours.append((i+1, j))
            if j > 0 and not self._cells[i][j-1].visited:
                neighbours.append((i, j-1))
            if j < self.rows - 1 and not self._cells[i][j+1].visited:
                neighbours.append((i, j+1))
            if len(neighbours) == 0:
                self._draw_cell(i, j)
                return
            next_i, next_j = random.choice(neighbours)
            if next_i < i: # left
                self._cells[i][j].open_wall("left")
                self._cells[next_i][next_j].open_wall("right")
            elif next_i > i: # right
                self._cells[i][j].open_wall("right")
                self._cells[next_i][next_j].open_wall("left")
            elif next_j < j: # up
                self._cells[i][j].open_wall("top")
                self._cells[next_i][next_j].open_wall("bottom")
            elif next_j > j: # down
                self._cells[i][j].open_wall("bottom")
                self._cells[next_i][next_j].open_wall("top")
            self._break_walls(next_i, next_j)
        
    def _reset_cell_visited(self):
        for i in range(0, self.cols):
            for j in range(0, self.rows):
                self._cells[i][j].visited = False
     
   # def solve(self):
         
    
    '''
    Draws a cell at the given column and row index
    '''
    def _draw_cell(self, col, row):
        if self._window is None:
            return
        self._cells[col][row].draw()
        self._animate()
    
    '''
    Refreshes the window, and waits for a short time to allow the
    animation to be seen
    '''
    def _animate(self):
        if self._window is None:
            return
        self._window.redraw()
        time.sleep(0.01)
        