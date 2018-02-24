import copy


class Node:
    '''
        Represents a 8-Puzzle state -- i.e. tile configuration
    '''

    # Static variable to be used to calculate the Hamming Distance
    GOAL_GRID = []

    # Constructor -- Takes a grid 
    def __init__(self, grid):
        self.grid = grid    # Note: a grid is a list of integers
        self._g = 0


    # G-score -- cost/distance from the start node
    @property
    def g_score(self):
        return self._g
    @g_score.setter
    def g_score(self, value):
        self._g = value


    # Heuristic value -- Hamming distance (num of out-of-place tiles)
    @property
    def h_score(self):
        # Ensure that the Node.GOAL_GRID is populated
        if not Node.GOAL_GRID:
            raise ValueError

        res = 0
        # Count out-of-place tiles
        for i in range(len(self.grid)):
            if self.grid[i] != Node.GOAL_GRID[i]:
                res += 1
        return res
    #end-h_score



        
    @property
    def f_score(self):
        return self.g_score + self.h_score

    # Generates the states that correspond to the possbile moves
    def get_neighbors(self):
        '''
            Note: this function creates new Nodes (8-Puzzle states) that
                  that result from moving the blank tile to each possible direction
        '''
        blankPosition = self.grid.index(0)
        left = None
        up = None
        right = None
        down = None

        # Left -- move the blank tile to the left (if possible)
        #-----------------------------------------------------
        # Check if the blank can be moved to the left
        if blankPosition not in [0, 3, 6]:
            # Create a deep copy
            tempGrid = copy.deepcopy(self.grid) 

            # Swap the blank tile with the tile on the LEFT
            temp = tempGrid[blankPosition]
            tempGrid[blankPosition] = tempGrid[blankPosition - 1]
            tempGrid[blankPosition - 1] = temp
            # Create the Node object
            left = Node(tempGrid)

        # Up -- move the blank tile up (if possible)
        #-----------------------------------------------------
        # Check if the blank can be moved up
        if blankPosition not in [0, 1, 2]:
            # Create a deep copy
            tempGrid = copy.deepcopy(self.grid) 

            # Swap the blank tile with the tile on the up
            temp = tempGrid[blankPosition]
            tempGrid[blankPosition] = tempGrid[blankPosition - 3]
            tempGrid[blankPosition - 3] = temp
            # Create the Node object
            up = Node(tempGrid)

        # Right -- move the blank tile to the right (if possible)
        #-----------------------------------------------------
        # Check if the blank can be moved to the right
        if blankPosition not in [2, 5, 8]:
            # Create a deep copy
            tempGrid = copy.deepcopy(self.grid) 

            # Swap the blank tile with the tile on the right
            temp = tempGrid[blankPosition]
            tempGrid[blankPosition] = tempGrid[blankPosition + 1]
            tempGrid[blankPosition + 1] = temp
            # Create the Node object
            right = Node(tempGrid)

        # Down -- move the blank tile down (if possible)
        #-----------------------------------------------------
        # Check if the blank can be moved down
        if blankPosition not in [6, 7, 8]:
            # Create a deep copy
            tempGrid = copy.deepcopy(self.grid) 

            # Swap the blank tile with the tile on the down
            temp = tempGrid[blankPosition]
            tempGrid[blankPosition] = tempGrid[blankPosition + 3]
            tempGrid[blankPosition + 3] = temp
            # Create the Node object
            down = Node(tempGrid)

        return [left, up, right, down]
    #end-get_neighbors

    # Prints the contents of the grid
    def print_grid(self):
        print(self.grid[0:3])       # Row 0
        print(self.grid[3:6])       # Row 1
        print(self.grid[6:9])       # Row 2
        print()

#end-class Node


class PuzzleSolver:
    '''
        Implements the A* algorithm
    '''
    def __init__(self, startNode, goalNode):
        self.start = startNode
        Node.GOAL_GRID = goalNode.grid           # Set the static variable GOAL_GRID

    def a_star():
        print("")
    #end-a_star


#end-class PuzzleSolver


def read_inputs(fileName):
    start = []
    goal = []
    with open(fileName) as f:
        #Read start grid
        for l in range(3):
            for x in next(f).split(" "):
                if x != "\n":
                    start.append(int(x))
        
        next(f) # Skip break

        #Read goal state's grid
        for l in range(3):
            for x in next(f).split(" "):
                if x != "\n":
                    goal.append(int(x))
    #end-with
    return start, goal
#end-read_inputs
               
        
        


def main():
    print("Starting Main")

    # Read inputs -- the start and goal states
    #-------------------------------------------
    start, goal = read_inputs("input.txt")
    startNode = Node(start)
    goalNode = Node(goal)


    # Create the PuzzleSolver
    puzzleSolver = PuzzleSolver(startNode, goalNode)
    

    startNode.print_grid()
    for x in startNode.get_neighbors():
        if x is not None:
            x.print_grid()

    # # Invoke solver
    # # puzzleSolver.a_star()

    print("Ending Main")

#end-main


# Test Driver
def test():
    print("Hello World")

    grid = [0,1,2,
            3,4,5,
            6,7,8]

    testNode = Node(grid)
    testNode.print_grid()





# Invoke driver
# test()
main()
