
# Sudoku Solver

The objective of the project was to create an algorithm which solves sudoku boards, as observed in the lecture notes this type of challenge is an example of a constraint satisfaction problem. The first attempt of implementing such an algorithm followed the procedure outlined below.

### 1. Virtualize the Board

The dimensions of the board must first be defined before implementing the dynamics of the game, hence the function below takes an input of a  9x9 array and splits it into a list of dictionaries, with both row-wise ordering & column-wise ordering then concates them into a single list. Where the keys of the dictionary are positions on the board and the value corresponds to the value within the cell.

```bash
def board_cells(Grid):
    rows = []
    columns = []
    for x in range(0,9):
        row = {}
        column = {}
        for y in range(0,9):
            row[(x,y)] = Grid[x][y]
            column[(x,y)] = Grid[y][x]
        rows.append(row)
        columns.append(column)
    all_cells = rows + columns
    return all_cells
```

A sudoku board is also split into smaller 3x3 squares which need to be recognised, hence the following function.

```bash

def cell_square(row, column, grid):
        row, column = row // 3, column // 3
        board = grid.tolist()
        square = (board[row*3][column*3:column*3+3]+board[(row*3) +1][column*3:((column*3)+3)] + board[(row*3) +2][column*3:((column*3)+3)])
        return square
```

### 2. Constraint propagation

This function implements the main propagation of constraints – no 2 identical values between 1 and 9 can occupy the same row or column or square. This was implemented by finding the resultant set between the set of values already existing within the board cells and taking it away from the set of possible values (1 to 9), the resultant set is therefore the set of valid values which can be placed within a given cell.

```bash
def poss_cell_state(cell_row, cell_column, Grid):
    
    if Grid[cell_row][cell_column] != 0:
        return [None],[None],[None]

    cell_positions = {}
    exist = []
    all_cells = board_cells(Grid)
    square_values = cell_square(cell_row, cell_column,Grid)
    
    for cell in all_cells:
        if (cell_row, cell_column) in cell.keys():
            cell_positions.update(cell)
           

    for cell_pos in cell_positions:                 
        if not cell_positions[cell_pos] == 0:
            exist.append(cell_positions[cell_pos])

    rest = list(set(elements) - set(exist) - set(square_values)) 
    
    return rest, exist, cell_positions
```

### 3. Agent path

The behaviour in regards to how the search algorithm should move across the board and at boundaries was defined to move along the row one cell position at a time unless in the last column, otherwise move to the first column in the row below, effectively creating a boundary condition, this function is only called when attempting to fill in a cell.

```bash
def new_cell(row, column):
     if column == 8:
            if row == 8:
                new_row = row
                new_column = column 
            else:
                new_column = 0
                new_row = row + 1
     else:
        new_row = row
        new_column = column + 1
     return new_row, new_column
```

### 4. End states

Methods corresponding to all possible final game states:

  1. Firstly, whether the start state is valid.
  
   &#39;valid\_board&#39;, checks whether the elements within each row and column are unique and if so, return a boolean value.

```bash
def valid_board(board):
    
    board_rows = board.tolist()
    board_columns = (np.transpose(np.array(board))).tolist()
    
    for i in range(9):
        for j in range(1,10):
            if board_rows[i].count(j) > 1:
                return False
            if board_columns[i].count(j) > 1:
                return False
    return True
```

  2. Secondly the end state where the board has been filled in accordance with the game constraints.

The value returned from this function is by default set to True but is otherwise changed to false if any cell contains a 0. This method relies on the constraints defined in section 3 upholding, as there is no check on the actual board other than the board being filled.

```bash
def is_complete(Grid):
    grid_complete = True
    for cell in Grid:
        grid_complete = grid_complete and not (0 in cell)
    return grid_complete
```

  3. Lastly, the algorithm has met a point in the board where no valid inputs are available, the board is unsolvable.

This end state is indirectly implemented by use of a recursive count condition in the main function, if this count is exceeded the algorithm will return an array of -1&#39;s. This condition is not strictly true for invalid inputs but was implemented as it enforces a given computational efficiency to the algorithm while also correctly returning unsolvable boards by recursively attempting to fill cells with no values until the recursive cap is met.

### 5. Recursive depth search

A search which recursively calls the grid attempting to fill each cell with values which are valid, found from the poss\_cell\_state() function, but firstly checks if game end states are met whether the board is complete, and whether the recursive count limit has been met, which increments by 1 each call.

```bash
def recursive_search(last_Grid, row, column):
    
    global x, recursive_count, elements
    
    if is_complete(last_Grid):
        x = last_Grid
        return None
    
    cell_state,_,_  = poss_cell_state(row, column, last_Grid)
   
    if recursive_count <= 500000:
        
        for cell in cell_state:
            Grid = deepcopy(last_Grid)
            if last_Grid[row][column] == 0:
                Grid[row][column] = cell
            
            new_row, new_column = new_cell(row, column)
            #new_row, new_column = priority_cell(last_Grid)
            
            recursive_count +=1
            recursive_search(Grid, new_row, new_column)
    else:
        x = np.array([[-1 for _ in range(9)] for _ in range(9)])
```

### 6. Main function

A main function which initialises all global variables used within the algorithm, states the possible values the board can take and checks whether the board is value before attempting to solve it, otherwise returning an array of -1&#39;s.

```bash
def sudoku_solver(sudoku):
    
    global x, recursive_count, elements
    elements = [1,2,3,4,5,6,7,8,9]
    recursive_count = 0
    x = np.array([[-1 for _ in range(9)] for _ in range(9)])
    
    if valid_board(sudoku):
        recursive_search(sudoku,0,0)
        
    return x
```

# Summary

Depth-first search 


The code sectioned above is an attempt at implementing a sudoku solver by depth-first searching through a set of solutions for each empty cell from the board stored by the data structures defined in [section 1](#1-virtualize-the-board). The set of possible solutions a given cell can take is deduced by use of a specific set of constraints defined by the functions implemented in [section 2](#2-constraint-propagation) namely values within rows, columns and 3x3 squares must belong to a unique set of values between 1 and 9. 

The algorithm will indiscrimnately choose a value from the set of a possible solutions for a given cell and then move onto the next avaliable cell, instructured by the simplistic path defined in [section 3](#3-agent-path) where the solving agent will sequentially move across a row until a boundary corresponding to the last column is exceeded, consquentially moving to the row below. 

The algorithm will continue down the current branch of solutions until an empty cell is met which can not be filled with a value while simultaneously not violating the constraints of the system. As a result the algorithm will return to an earlier state of the system which was memorized and attempt an alternative branch by filling this previously occupied state with a different value, and continue to backtrack until one of the possible three end states are met, as vizulaized in the gif below. 

![Backtracking-gif](https://github.bath.ac.uk/raw/ja702/random-uploads/master/Sudoku_solved_by_bactracking.gif?token=AAAAMP4UVGIHBBURWZ75F43AJY7KQ)#

Image Reference: (By Simpsons contributor - Program written in Java, letter images made in Photoshop, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=29034832)

Firstly, the algorithm will return a completed board if no cells within the virtualized board contain a zero with the arrangement of numbers also staying within the constraints of the system. Secondly, whether all possible branches have been explored with each returning a cell with no possible values, in this case an array of -1's will be returned. Lastly, before each recrusive call the input board is checked whether it is a valid sudoku board.

All individual functions are brought together in a main function which initiates the solving algorithm after defining all global variables and setting the default solution to an array of -1's, as previewed in [section 6](#6-main-function).


# Evaluation

After testing I found this algorithm struggled to solve some of the boards in the hard category within the desired time limit, this was evidently from the large number of recursive counts due to the agents movement, where the next cell chosen within a search is the next sequential cell along in a row or the row below if in the last column, which leads to a larger number of possible branches being explored before a solution is found.

For instance, a test was conducted with a board which had only the last cell missing a value and a counter with a print statement which displayed each recursion count, the solver went through 81 recursions to reach the cell and then attempt to solve it.


![Sequential cell algorithm](https://github.bath.ac.uk/raw/ja702/random-uploads/master/Capture.JPG?token=AAAAMPZIKIUYVJWJTS5ZLSTAJKL4Y)   

Hence, in an effort to reduce the time complexity, the algorithm was adapted to observe the set of possible values for all cells, as opposed to sequentially &#39;depth searching&#39; all possible values of a single cell, then targeting the cells with the smallest set, ultimately creating a priority search of the shortest branches for solutions, which is how we would attempt a sudoku board in reality.

```bash

def priority_cell(grid):
    
    grid_state = {}
    for x in range(0,9):
        for y in range(0,9):
            if grid[x][y] == 0:
                grid_state[(x,y)] = grid[x][y]
    
    p_cell = {}
    
    for key in grid_state.keys():
        p_cell_value,_,_ = poss_cell_state(key[0], key[1], grid)
        p_cell[key] = p_cell_value
    
    (p_row, p_col) = list({x:y for x,y in sorted(p_cell.items(),key=lambda item: sum(item[1]))})[0]
    
    return p_row, p_col

```

 However, after implementing this change i found the time complexity to actually increase on particular boards in the hard category, resulting in all the boards being correctly completed but some requiring a large amount of time.
    
![Slow algorithm](https://github.bath.ac.uk/raw/ja702/random-uploads/master/Capture2.JPG?token=AAAAMP2V5C7YLOMHLTPGXPTAJKVTK)

I believe the long computational time is due to inefficiently updating states, as each recursive call the board is recreated in the code snippet above, i.e. 'grid_state', as opposed to creating a single object and simply updating it, i believe this alteration would have a great effect on decreasing the computational time but may require one to restructure the entire code to utilize object orientated programming attributes.

    
