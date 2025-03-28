import unittest 
from maze import Maze

class TestMaze(unittest.TestCase):
    def test_maze_create_small(self):
        cols = 2
        rows = 2
        maze = Maze(0, 0, rows, cols, 10, 10)
        self.assertEqual(len(maze._cells), cols)
        self.assertEqual(len(maze._cells[0]), rows)
     
    def test_maze_create_large(self):   
        cols = 50
        rows = 50
        maze = Maze(0, 0, rows, cols, 10, 10)
        self.assertEqual(len(maze._cells), cols)
        self.assertEqual(len(maze._cells[0]), rows)
        
    def test_maze_create_entrance_exit(self):
        cols = 2
        rows = 2
        maze = Maze(0, 0, rows, cols, 10, 10)
        maze._make_entrance_exit()
        self.assertFalse(maze._cells[0][0].top)
        self.assertFalse(maze._cells[1][1].bottom)
        
    def test_maze_break_walls(self):
        cols = 2
        rows = 2
        maze = Maze(0, 0, rows, cols, 10, 10)
        maze._break_walls(0, 0)
        self.assertTrue(maze._cells[0][0].visited)
        self.assertTrue(maze._cells[1][0].visited or maze._cells[0][1].visited)
    
    def test_maze_reset_visited(self):
        cols = 2
        rows = 2
        maze = Maze(0, 0, rows, cols, 10, 10)
        maze._cells[0][0].visited = True
        maze._reset_cell_visited()
        self.assertFalse(maze._cells[0][0].visited)
    
if __name__ == "__main__":
    unittest.main()
