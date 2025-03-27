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
    
if __name__ == "__main__":
    unittest.main()
