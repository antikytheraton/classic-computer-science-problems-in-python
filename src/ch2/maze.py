from enum import Enum
from typing import List, NamedTuple, Callable, Optional
import random
from math import sqrt


class Cell(str, Enum):
    '''
        Our maze will be a two-dimesional grid of Cells.
        A Cell is an Enum with str values representing
        the spaces on the maze.
    '''
    EMPTY = ' '
    BLOCKED = 'X'
    START = 'S'
    GOAL = 'G'
    PATH = '*'


class MazeLocation(NamedTuple):
    '''
        We will need a way to refer to an individual location
        in the maze. This will be simply be a NamedTuple with
        properties representing the row and column of the
        location in question.
    '''

    row: int
    column: int


class Maze:
    '''
        Generating a random maze.

        Our maze class will internally keep track of a grid (a list of lists)
        representing its state. It will also have instance variables for the
        number of rows, number of columns, start location. Its grid will be
        randomly filled with blocked cells.

        The maze that is generated should be fairly sparse so that there is almost
        always a path from a given starting point to a given goal location. Well
        let the caller of a new maze decide on the exact sparseness, but we will
        provide a default value of 20% blocked. When a random number beats the 
        threshold of the sparseness parameter in question, we will simply replace
        an empty space with a wall. If we do this for every possible place place
        in the maze, statistically, the sparse of the maze as a whole will approximate
        the sparseness parameter supplied.
    '''

    def __init__(self, rows: int = 10, columns: int = 10,
        sparseness: float = 0.2, start: MazeLocation = MazeLocation(0,0),
        goal: MazeLocation = MazeLocation(9,9)) -> None:

        # initialize basic instance variables
        self._rows: int = rows
        self._columns: int = columns
        self.start: MazeLocation = start
        self.goal: MazeLocation = goal
        # fill the grid with empty cells
        self._grid: List[List[Cell]] = [[Cell.EMPTY for c in range(columns)] for r in range(rows)]
        # populate the grid with blocked cells
        self._randomly_filled(rows, columns, sparseness)
        # fill the start and goal locations in
        self._grid[start.row][start.column] = Cell.START
        self._grid[goal.row][goal.column] = Cell.GOAL

    def _randomly_filled(self, rows:int, columns: int, sparseness: float):
        for row in range(rows):
            for column in range(columns):
                if random.uniform(0, 1.0) < sparseness:
                    self._grid[row][column] = Cell.BLOCKED

    def __str__(self) -> str:
        output: str = ''
        for row in self._grid:
            output += ''.join([c.value for c in row]) + '\n'
        return output

    def goal_test(self, ml: MazeLocation) -> bool:
        '''
            Test if we reached the goal cell.
        '''
        return ml == self.goal

    def successors(self, ml: MazeLocation) -> List[MazeLocation]:
        '''
            We can move horizontally and vertically one space at a time from
            a given space in the maze.
        '''
        locations: List[MazeLocation] = []
        if ml.row + 1 < self._rows and self._grid[ml.row + 1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row + 1, ml.column))
        if ml.row - 1 >= 0 and self._grid[ml.row - 1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row - 1,ml.column))
        if ml.column + 1 < self._columns and self._grid[ml.row][ml.column + 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row,ml.column + 1))
        if ml.column - 1 >= 0 and self._grid[ml.row][ml.column - 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row,ml.column - 1))
        return locations

    def mark(self, path: List[MazeLocation]):
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.PATH
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

    def clear(self, path: List[MazeLocation]):
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.EMPTY
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

