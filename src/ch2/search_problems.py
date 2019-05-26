
from typing import List, NamedTuple, Callable, Optional
from maze import Maze, MazeLocation
from generic_search import(
    dfs,
    node_to_path, Node
)


if __name__ == "__main__":
    # Test DFS
    m: Maze = Maze()
    print(m)
    solution1: Optional[Node[MazeLocation]] = dfs(
        m.start, m.goal_test, m.successors
    )
    if solution1 is None:
        print('No solution found using depth-first search!')
    else:
        path1: List[MazeLocation] = node_to_path(solution1)
        m.mark(path1)
        print(m)
        m.clear(path1)
