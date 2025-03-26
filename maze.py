from graphics import Cell
import time

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
    def __init__(self, window, m_x, m_y, rows, cols, cell_size_x, cell_size_y):
        self._m_x = m_x # x pos of maze origin
        self.m_y = m_y # y pos of maze origin
        self.rows = rows
        self.cols = cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._cells = []
        self._window = window
        self._create_cells()
    
    '''
    Populates the cell list, and then draws them all on the canvas
    '''
    def _create_cells(self):
        for i in range(0, self.cols):
            column = []
            for j in range(0, self.rows):
                cell_left_x = self._m_x + i * self.cell_size_x
                cell_right_x = self._m_x + (i + 1) * self.cell_size_x
                cell_top_y = self.m_y + j * self.cell_size_y
                cell_bottom_y = self.m_y + (j + 1) * self.cell_size_y
                cell = Cell(self._window, cell_left_x, cell_top_y, cell_right_x, cell_bottom_y)
                column.append(cell)
            self._cells.append(column)
        # Then draw them all
        for i in range(0, self.cols):
            for j in range(0, self.rows):
                self._draw_cell(i, j)
                
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
        time.sleep(0.05)
        