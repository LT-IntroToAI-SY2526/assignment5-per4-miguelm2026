# Assignment 5 Write up

Assignment 5 can be broken up into the following parts:
1. Import the Necessary Modules:
- `copy`: For creating deep copies of objects
- `Stack` and `Queue`: Custom implementations for DFS and BFS operations
2. Utility Functions: 
- `remove_if_exists`: Removes a specified element from a list if it exists, which is used to remove the possibilites from a cell
3. Board Class:
- Represents the Sudoku board
- Consists of functions that will find the most constrained cell, and update the board, which eliminates possible solutions
4. DFS & BFS Functions:
- `DFS`: Uses depth-first search to solve the Sudoku puzzle. It works by trying to fill the most constrained cell with potential values until a solution is found or backtracks if a mistake is made
- `BFS`: Uses breadth-first search to solve the Sudoku puzzle in a similar fashion to DFS but explores nodes level by level
5. Main Execution:
- Defines two different sets of initial moves for Sudoku puzzles
- Uses both DFS and BFS to solve each puzzle and prints the results


After completing the assignment, answer the following reflection questions:

## Reflection Questions

1. What are some things that you learned through this assignment? Think about the concepts of backtracking, constraint satisfaction, and search algorithms. Were there any particular challenges you faced while implementing the Board class methods or the DFS/BFS functions? How did you overcome them?

Through this assignment I was able to learn backtracking to solve problems that require structuring to solve, such as the Sudoku. One of the ideas was that instead of just randomly guessing, the solver would use the constraints that are there to reduce the possibilites and make searching more efficent. Also, I learned how DFS and BFS are used when they are appled in a large space, DFS goes into one possible solution path before it backtracks, and BFS expolores all the possibilites. While there were both, DFS was more suited to backtrack, and BFS caused a little bit more issues. Some challenges that were present was getting the board to update in the correct order, and removing values consistenly. Deugging was used when stuff would end up in the wrong cell, and cause errores, but it helped minimize these problems in the end.


2. How can you apply what you learned in this assignment to future programs or projects? Consider other types of problems that involve searching through possibilities, making decisions, and backtracking when those decisions don't work out. Can you think of real-world scenarios where DFS or BFS might be useful? What about other constraint satisfaction problems?

Search algorithsm such as DFS and BFS could be used for pathfinidng such as mazes, maps and etc to get it done. Backtracking would also be used for puzzle games to ake sure that tasks are run correctly and are on track to be correct. Sudoku is just one thing, that many of these same concepts with AI can be applied to if used correctly and thoroughly.

3. Explain how the Stack and Queue classes work and why they are important for DFS and BFS algorithms. Describe the difference between LIFO (Last In First Out) and FIFO (First In First Out) data structures. How does using a Stack versus a Queue change the way the search algorithm explores possible solutions? Why is one data structure better suited for depth-first search and the other for breadth-first search?

LIFO - Most recently added is the first one removed. Better for DFS becusae it searches for the deepest branch before it backs up. 

FIFO - The earliest item is removed first. Better for BFS because it explores one layer at a time before moving deeper.

With a stack, DFS dives quickly into one path, and used less memory while supporting backtracking. DFS is better to find soutions faster. 

With a Queue, BFS explores all the possibilites before it moves onto the next, it guarenttes the shortest solution path but with memory. 

These two srategies depend entirely on the things that are provided, and understanding them gives better control to the explorations required to run efficent algorithms.