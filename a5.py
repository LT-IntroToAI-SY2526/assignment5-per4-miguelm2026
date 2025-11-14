import copy
from typing import List, Any, Tuple
from collections import deque


# ----- Stack and Queue helper classes -----
class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop() if not self.is_empty() else None

    def is_empty(self):
        return len(self.data) == 0


class Queue:
    def __init__(self):
        self.data = deque()

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.popleft() if not self.is_empty() else None

    def is_empty(self):
        return len(self.data) == 0


# ----- Helper -----
def remove_if_exists(lst: Any, elem: Any) -> None:
    if isinstance(lst, list) and elem in lst:
        lst.remove(elem)


# ----- Board class -----
class Board:
    def __init__(self):
        self.size: int = 9
        self.num_nums_placed: int = 0
        self.rows: List[List[Any]] = [
            [list(range(1, 10)) for _ in range(self.size)] for _ in range(self.size)
        ]

    def __str__(self) -> str:
        row_str = ""
        for r in self.rows:
            row_str += f"{r}\n"
        return f"num_nums_placed: {self.num_nums_placed}\nboard (rows): \n{row_str}"

    def print_pretty(self):
        row_str = ""
        for i, r in enumerate(self.rows):
            if not i % 3:
                row_str += " -------------------------\n"
            for j, x in enumerate(r):
                row_str += " | " if not j % 3 else " "
                row_str += "*" if isinstance(x, list) else f"{x}"
            row_str += " |\n"
        row_str += " -------------------------\n"
        print(f"num_nums_placed: {self.num_nums_placed}\nboard (rows): \n{row_str}")

    def subgrid_coordinates(self, row: int, col: int) -> List[Tuple[int, int]]:
        subgrids = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
        return [(r, c) for c in subgrids[col // 3] for r in subgrids[row // 3]]

    def find_most_constrained_cell(self) -> Tuple[int, int]:
        min_len = 10
        min_pos = None
        for r in range(self.size):
            for c in range(self.size):
                cell = self.rows[r][c]
                if isinstance(cell, list) and len(cell) < min_len and len(cell) > 0:
                    min_len = len(cell)
                    min_pos = (r, c)
        return min_pos

    def failure_test(self) -> bool:
        for r in range(self.size):
            for c in range(self.size):
                if isinstance(self.rows[r][c], list) and len(self.rows[r][c]) == 0:
                    return True
        return False

    def goal_test(self) -> bool:
        return self.num_nums_placed == 81

    def update(self, row: int, column: int, assignment: int) -> None:
        # if already assigned, skip
        if not isinstance(self.rows[row][column], list):
            return

        # assign value
        self.rows[row][column] = assignment
        self.num_nums_placed += 1

        # update row and column
        for i in range(self.size):
            remove_if_exists(self.rows[row][i], assignment)
            remove_if_exists(self.rows[i][column], assignment)

        # update subgrid
        for r, c in self.subgrid_coordinates(row, column):
            remove_if_exists(self.rows[r][c], assignment)


# ----- DFS and BFS -----
def DFS(state: Board) -> Board:
    stack = Stack()
    stack.push(state)

    while not stack.is_empty():
        board = stack.pop()
        if board.goal_test():
            return board
        if board.failure_test():
            continue

        next_cell = board.find_most_constrained_cell()
        if not next_cell:
            continue
        r, c = next_cell
        for val in board.rows[r][c]:
            new_board = copy.deepcopy(board)
            new_board.update(r, c, val)
            stack.push(new_board)
    return None


def BFS(state: Board) -> Board:
    queue = Queue()
    queue.push(state)

    while not queue.is_empty():
        board = queue.pop()
        if board.goal_test():
            return board
        if board.failure_test():
            continue

        next_cell = board.find_most_constrained_cell()
        if not next_cell:
            continue
        r, c = next_cell
        for val in board.rows[r][c]:
            new_board = copy.deepcopy(board)
            new_board.update(r, c, val)
            queue.push(new_board)
    return None


# ----- MAIN -----
if __name__ == "__main__":
    print("<<<<<<<<<<<<<< Solving Sudoku Puzzle >>>>>>>>>>>>>>")

    # Partial Sudoku Puzzle
    initial_moves = [
        (0, 0, 5), (0, 1, 3), (0, 4, 7),
        (1, 0, 6), (1, 3, 1), (1, 4, 9), (1, 5, 5),
        (2, 1, 9), (2, 2, 8), (2, 7, 6),
        (3, 0, 8), (3, 4, 6), (3, 8, 3),
        (4, 0, 4), (4, 3, 8), (4, 5, 3), (4, 8, 1),
        (5, 0, 7), (5, 4, 2), (5, 8, 6),
        (6, 1, 6), (6, 6, 2), (6, 7, 8),
        (7, 3, 4), (7, 4, 1), (7, 5, 9), (7, 8, 5),
        (8, 4, 8), (8, 7, 7), (8, 8, 9),
    ]

    b = Board()
    for move in initial_moves:
        b.update(*move)

    print("<<<<< Initial Board >>>>>")
    b.print_pretty()

    print("\n<<<<<<<<<<<<<< Solving with DFS >>>>>>>>>>>>>>")
    solved_dfs = DFS(copy.deepcopy(b))
    solved_dfs.print_pretty()

    print("\n<<<<<<<<<<<<<< Solving with BFS >>>>>>>>>>>>>>")
    solved_bfs = BFS(copy.deepcopy(b))
    solved_bfs.print_pretty()

    print("\nGoal test (DFS):", solved_dfs.goal_test())
    print("Goal test (BFS):", solved_bfs.goal_test())


