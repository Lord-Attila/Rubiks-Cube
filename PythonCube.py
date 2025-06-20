import copy
import numpy as np
from Cube import pruning_table


class RubiksCube:
    def __init__(self):
        self.greenface = [["g", "g", "g"], ["g", "g", "g"], ["g", "g", "g"]]
        self.whiteface = [["w", "w", "w"], ["w", "w", "w"], ["w", "w", "w"]]
        self.blueface = [["b", "b", "b"], ["b", "b", "b"], ["b", "b", "b"]]
        self.orangeface = [["o", "o", "o"], ["o", "o", "o"], ["o", "o", "o"]]
        self.redface = [["r", "r", "r"], ["r", "r", "r"], ["r", "r", "r"]]
        self.yellowface = [["y", "y", "y"], ["y", "y", "y"], ["y", "y", "y"]]

    def isSolved(self):
        if (self.greenface == [["g", "g", "g"], ["g", "g", "g"], ["g", "g", "g"]]):
            if (self.whiteface == [["w", "w", "w"], ["w", "w", "w"], ["w", "w", "w"]]):
                if (self.blueface == [["b", "b", "b"], ["b", "b", "b"], ["b", "b", "b"]]):
                    if (self.orangeface == [["o", "o", "o"], ["o", "o", "o"], ["o", "o", "o"]]):
                        if (self.redface == [["r", "r", "r"], ["r", "r", "r"], ["r", "r", "r"]]):
                            if (self.yellowface == [["y", "y", "y"], ["y", "y", "y"], ["y", "y", "y"]]):
                                return True
        return False

    # right side up
    def r(self):
        tempred = copy.deepcopy(self.redface)
        tempgreen = copy.deepcopy(self.greenface)
        tempwhite = copy.deepcopy(self.whiteface)
        tempblue = copy.deepcopy(self.blueface)
        tempyellow = copy.deepcopy(self.yellowface)

        for i in range(3):
            tempred[0][i] = self.redface[2 - i][0]
        for i in range(3):
            tempred[2][2 - i] = self.redface[i][2]
        for i in range(3):
            tempred[i][0] = self.redface[2][i]
        for i in range(3):
            tempred[i][2] = self.redface[0][i]
        for i in range(3):
            tempwhite[i][2] = self.greenface[i][2]
        for i in range(3):
            tempblue[2 - i][0] = self.whiteface[i][2]
        for i in range(3):
            tempyellow[i][0] = self.blueface[i][0]
        for i in range(3):
            tempgreen[i][2] = self.yellowface[2 - i][0]
        self.redface = tempred.copy()
        self.blueface = tempblue.copy()
        self.whiteface = tempwhite.copy()
        self.yellowface = tempyellow.copy()
        self.greenface = tempgreen.copy()

    # right side down
    def rprime(self):
        self.r()
        self.r()
        self.r()

    # left side down
    def l(self):
        temporange = copy.deepcopy(self.orangeface)
        tempgreen = copy.deepcopy(self.greenface)
        tempwhite = copy.deepcopy(self.whiteface)
        tempblue = copy.deepcopy(self.blueface)
        tempyellow = copy.deepcopy(self.yellowface)

        for i in range(3):
            temporange[0][i] = self.orangeface[2 - i][0]
        for i in range(3):
            temporange[2][2 - i] = self.orangeface[i][2]
        for i in range(3):
            temporange[i][0] = self.orangeface[2][i]
        for i in range(3):
            temporange[i][2] = self.orangeface[0][i]
        for i in range(3):
            tempwhite[i][0] = self.blueface[2 - i][2]
        for i in range(3):
            tempblue[i][2] = self.yellowface[i][2]
        for i in range(3):
            tempyellow[i][2] = self.greenface[2 - i][0]
        for i in range(3):
            tempgreen[i][0] = self.whiteface[i][0]
        self.orangeface = temporange.copy()
        self.blueface = tempblue.copy()
        self.whiteface = tempwhite.copy()
        self.yellowface = tempyellow.copy()
        self.greenface = tempgreen.copy()

    def lprime(self):
        self.l()
        self.l()
        self.l()

    def f(self):
        temporange = copy.deepcopy(self.orangeface)
        tempgreen = copy.deepcopy(self.greenface)
        tempwhite = copy.deepcopy(self.whiteface)
        tempred = copy.deepcopy(self.redface)
        tempyellow = copy.deepcopy(self.yellowface)

        for i in range(3):
            tempgreen[0][i] = self.greenface[2 - i][0]
        for i in range(3):
            tempgreen[2][2 - i] = self.greenface[i][2]
        for i in range(3):
            tempgreen[i][0] = self.greenface[2][i]
        for i in range(3):
            tempgreen[i][2] = self.greenface[0][i]

        for i in range(3):
            tempwhite[2][i] = self.orangeface[2 - i][2]
        for i in range(3):
            temporange[i][2] = self.yellowface[2][2 - i]
        for i in range(3):
            tempyellow[2][i] = self.redface[i][0]
        for i in range(3):
            tempred[i][0] = self.whiteface[2][i]
        self.orangeface = temporange.copy()
        self.redface = tempred.copy()
        self.whiteface = tempwhite.copy()
        self.yellowface = tempyellow.copy()
        self.greenface = tempgreen.copy()

    def fprime(self):
        self.f()
        self.f()
        self.f()

    def u(self):
        temporange = copy.deepcopy(self.orangeface)
        tempgreen = copy.deepcopy(self.greenface)
        tempwhite = copy.deepcopy(self.whiteface)
        tempred = copy.deepcopy(self.redface)
        tempblue = copy.deepcopy(self.blueface)

        for i in range(3):
            tempwhite[0][i] = self.whiteface[2 - i][0]
        for i in range(3):
            tempwhite[2][2 - i] = self.whiteface[i][2]
        for i in range(3):
            tempwhite[i][0] = self.whiteface[2][i]
        for i in range(3):
            tempwhite[i][2] = self.whiteface[0][i]

        for i in range(3):
            tempblue[0][i] = self.orangeface[0][i]
        for i in range(3):
            temporange[0][i] = self.greenface[0][i]
        for i in range(3):
            tempgreen[0][i] = self.redface[0][i]
        for i in range(3):
            tempred[0][i] = self.blueface[0][i]
        self.orangeface = temporange.copy()
        self.redface = tempred.copy()
        self.whiteface = tempwhite.copy()
        self.blueface = tempblue.copy()
        self.greenface = tempgreen.copy()

    def uprime(self):
        self.u()
        self.u()
        self.u()

    def b(self):
        temporange = copy.deepcopy(self.orangeface)
        tempblue = copy.deepcopy(self.blueface)
        tempwhite = copy.deepcopy(self.whiteface)
        tempred = copy.deepcopy(self.redface)
        tempyellow = copy.deepcopy(self.yellowface)

        for i in range(3):
            tempblue[0][i] = self.blueface[2 - i][0]
        for i in range(3):
            tempblue[2][2 - i] = self.blueface[i][2]
        for i in range(3):
            tempblue[i][0] = self.blueface[2][i]
        for i in range(3):
            tempblue[i][2] = self.blueface[0][i]

        for i in range(3):
            tempwhite[0][i] = self.redface[i][2]
        for i in range(3):
            tempred[i][2] = self.yellowface[0][i]
        for i in range(3):
            tempyellow[0][i] = self.orangeface[2 - i][0]
        for i in range(3):
            temporange[i][0] = self.whiteface[0][2 - i]
        self.orangeface = temporange.copy()
        self.redface = tempred.copy()
        self.whiteface = tempwhite.copy()
        self.yellowface = tempyellow.copy()
        self.blueface = tempblue.copy()

    def bprime(self):
        self.b()
        self.b()
        self.b()

    def d(self):
        temporange = copy.deepcopy(self.orangeface)
        tempgreen = copy.deepcopy(self.greenface)
        tempblue = copy.deepcopy(self.blueface)
        tempred = copy.deepcopy(self.redface)
        tempyellow = copy.deepcopy(self.yellowface)

        for i in range(3):
            tempyellow[0][i] = self.yellowface[2 - i][0]
        for i in range(3):
            tempyellow[2][2 - i] = self.yellowface[i][2]
        for i in range(3):
            tempyellow[i][0] = self.yellowface[2][i]
        for i in range(3):
            tempyellow[i][2] = self.yellowface[0][i]

        for i in range(3):
            tempblue[2][i] = self.orangeface[2][i]
        for i in range(3):
            temporange[2][i] = self.greenface[2][i]
        for i in range(3):
            tempgreen[2][i] = self.redface[2][i]
        for i in range(3):
            tempred[2][i] = self.blueface[2][i]
        self.orangeface = temporange.copy()
        self.redface = tempred.copy()
        self.blueface = tempblue.copy()
        self.yellowface = tempyellow.copy()
        self.greenface = tempgreen.copy()

    def dprime(self):
        self.d()
        self.d()
        self.d()

    def rtwo(self):
        self.r()
        self.r()

    def btwo(self):
        self.b()
        self.b()

    def dtwo(self):
        self.d()
        self.d()

    def utwo(self):
        self.u()
        self.u()

    def ftwo(self):
        self.f()
        self.f()

    def ltwo(self):
        self.l()
        self.l()

    def print(self):
        for i in range(3):
            print(self.greenface[i])
        print()
        for i in range(3):
            print(self.whiteface[i])
        print()
        for i in range(3):
            print(self.blueface[i])
        print()
        for i in range(3):
            print(self.redface[i])
        print()
        for i in range(3):
            print(self.yellowface[i])
        print()
        for i in range(3):
            print(self.orangeface[i])
        print()

    edge_positions = [
        (("whiteface", (2, 1)), ("greenface", (0, 1))),
        (("whiteface", (1, 2)), ("redface", (0, 1))),
        (("whiteface", (0, 1)), ("blueface", (0, 1))),
        (("whiteface", (1, 0)), ("orangeface", (0, 1))),
        (("greenface", (1, 2)), ("redface", (1, 0))),
        (("greenface", (1, 0)), ("orangeface", (1, 2))),
        (("blueface", (1, 0)), ("orangeface", (1, 0))),
        (("blueface", (1, 2)), ("redface", (1, 2))),
        (("yellowface", (0, 1)), ("greenface", (2, 1))),
        (("yellowface", (1, 2)), ("redface", (2, 1))),
        (("yellowface", (2, 1)), ("blueface", (2, 1))),
        (("yellowface", (1, 0)), ("orangeface", (2, 1))),
    ]

    def edge_orientation_index(self):
        orientation = self.edge_orientations()
        n = 0
        for i in range(len(orientation)-1):
            n = (n << 1) | orientation[i]
        return n

    def corner_orientation_index(self):
        orientation = self.corner_orientations()
        n = 0
        for i in range(7):
            n = n * 3 + orientation[i]
        return n

    def corner_orientations(self):

        orientations = []

        if self.whiteface[0][0] == "w" or self.whiteface[0][0] ==  "y":
            orientations.append(0)
        elif self.orangeface[0][0] == "w" or self.orangeface[0][0] ==  "y":
            orientations.append(1)
        else:
            orientations.append(2)

        if self.whiteface[0][2] == "w" or self.whiteface[0][2] == "y":
            orientations.append(0)
        elif self.blueface[0][0] == "w" or self.blueface[0][0] == "y":
            orientations.append(1)
        else:
            orientations.append(2)

        if self.whiteface[2][0] == "w" or self.whiteface[2][0] == "y":
            orientations.append(0)
        elif self.greenface[0][0] == "w" or self.greenface[0][0] ==  "y":
            orientations.append(1)
        else:
            orientations.append(2)

        if self.whiteface[2][2] == "w" or self.whiteface[2][2] == "y":
            orientations.append(0)
        elif self.redface[0][0] == "w" or self.redface[0][0] == "y":
            orientations.append(1)
        else:
            orientations.append(2)

        if self.yellowface[2][2] == "w" or self.yellowface[2][2] == "y":
            orientations.append(0)
        elif self.greenface[2][0] == "w" or self.greenface[2][0] == "y":
            orientations.append(1)
        else:
            orientations.append(2)

        if self.yellowface[2][0] == "w" or self.yellowface[2][0] == "y":
            orientations.append(0)
        elif self.redface[2][0] == "w" or self.redface[2][0] == "y":
            orientations.append(1)
        else:
            orientations.append(2)

        if self.yellowface[0][2] == "w" or self.yellowface[0][2] == "y":
            orientations.append(0)
        elif self.orangeface[2][0] == "w" or self.orangeface[2][0] == "y":
            orientations.append(1)
        else:
            orientations.append(2)

        if self.yellowface[0][0] == "w" or self.yellowface[0][0] == "y":
            orientations.append(0)
        elif self.blueface[2][0] == "w" or self.blueface[2][0] == "y":
            orientations.append(1)
        else:
            orientations.append(2)
        return orientations


    def edge_orientations(self):

        orientations = []

        if self.whiteface[2][1] == "r" or self.whiteface[2][1] =="o":
            orientations.append(1)
        elif self.greenface[0][1] == "w" or self.greenface[0][1] == "y":
            orientations.append(1)
        else:
            orientations.append(0)

        if self.whiteface[0][1] == "r" or self.whiteface[0][1] == "o":
            orientations.append(1)
        elif self.blueface[0][1] == "w" or self.blueface[0][1] == "y":
            orientations.append(1)
        else:
            orientations.append(0)

        if self.whiteface[1][0] == "r" or self.whiteface[1][0] == "o":
            orientations.append(1)
        elif self.orangeface[0][1] == "w" or self.orangeface[0][1] ==  "y":
            orientations.append(1)
        else:
            orientations.append(0)

        if self.whiteface[1][2] == "r" or self.whiteface[1][2] == "o":
            orientations.append(1)
        elif self.redface[0][1] == "w" or self.redface[0][1] == "y":
            orientations.append(1)
        else:
            orientations.append(0)

        if self.yellowface[0][1] == "r" or self.yellowface[0][1] == "o":
            orientations.append(1)
        elif self.blueface[2][1] == "w" or self.blueface[2][1] == "y":
            orientations.append(1)
        else:
            orientations.append(0)

        if self.yellowface[1][0] == "r" or self.yellowface[1][0] == "o":
            orientations.append(1)
        elif self.redface[2][1] == "w" or self.redface[2][1] == "y":
            orientations.append(1)
        else:
            orientations.append(0)

        if self.yellowface[1][2] == "r" or self.yellowface[1][2] == "o":
            orientations.append(1)
        elif self.orangeface[2][1] == "w" or self.orangeface[2][1] == "y":
            orientations.append(1)
        else:
            orientations.append(0)

        if self.yellowface[2][1] == "r" or self.yellowface[2][1] == "o":
            orientations.append(1)
        elif self.greenface[2][1] == "w" or self.greenface[2][1] == "y":
            orientations.append(1)
        else:
            orientations.append(0)

        if self.orangeface[1][0] == "w" or self.orangeface[1][0] == "y":
            orientations.append(1)
        else:
            orientations.append(0)

        if self.orangeface[1][2] == "w" or self.orangeface[1][2] == "y":
            orientations.append(1)
        else:
            orientations.append(0)

        if self.redface[1][0] == "w" or self.redface[1][0] == "y":
            orientations.append(1)
        else:
            orientations.append(0)

        if self.redface[1][2] == "w" or self.redface[1][2] == "y":
            orientations.append(1)
        else:
            orientations.append(0)

        return orientations

    def edge_slice_index(self):
        orientation = self.edge_in_slice()
        n = 0
        for i in range(len(orientation)-1):
            n = (n << 1) | orientation[i]
        return n

    def edge_in_slice(self):
        edges_in_slice = []

        for i in [0,2]:
            if self.whiteface[i][1] == 'y' or self.whiteface[i][1] == 'w':
                edges_in_slice.append(0)
            else:
                edges_in_slice.append(1)
        for i in [0,2]:
            if self.whiteface[1][i] == 'y' or self.whiteface[1][i] == 'w':
                edges_in_slice.append(0)
            else:
                edges_in_slice.append(1)

        for i in [0,2]:
            if self.yellowface[i][1] == 'y' or self.yellowface[i][1] == 'w':
                edges_in_slice.append(0)
            else:
                edges_in_slice.append(1)
        for i in [0,2]:
            if self.yellowface[1][i] == 'y' or self.yellowface[1][i] == 'w':
                edges_in_slice.append(0)
            else:
                edges_in_slice.append(1)

        for i in [0,2]:
            if self.blueface[1][i] == 'y' or self.blueface[1][i] == 'w':
                edges_in_slice.append(0)
            else:
                edges_in_slice.append(1)

        for i in [0, 2]:
            if self.greenface[1][i] == 'y' or self.greenface[1][i] == 'w':
                edges_in_slice.append(0)
            else:
                edges_in_slice.append(1)

        return edges_in_slice



from collections import deque



def edge_pruning_table(objects, states):
    table_size = states ** objects

    pruning_table = [-1] * table_size #creates 1D -1 array with len(states^objects)

    solved_cube = RubiksCube() #creates base case of solved Rubik's cube
    start_index = solved_cube.edge_orientation_index() #finds the index of the orientation
                                                       # of the edges in the solved cube
    pruning_table[start_index] = 0  #sets the value of solved cube in array to zero.
                                    #ie no moves for edges to be oriented
    queue = deque()
    queue.append((solved_cube, 0)) #adds solved cube to queue with its depth
                                   #(number of moves to get to correct edge orientation)

    moves = ["r", "rprime", "rtwo",
             "l", "lprime", "ltwo",
             "f", "fprime", "ftwo",
             "u", "uprime", "utwo",
             "b", "bprime", "btwo",
             "d", "dprime", "dtwo"] #array of allowed moves on cube

    while queue: #while there is a cube in the queue continue the loop - this is our BFS algorithm
        cube, depth = queue.popleft() #removes cube and current number of moves from queue
        for move in moves:
            new_cube = copy.deepcopy(cube) #creates a copy of cube so that original cube can be reused
            getattr(new_cube, move)() #applys move to cube copy
            if (pruning_table[new_cube.edge_orientation_index()] == -1
                    or pruning_table[new_cube.edge_orientation_index()] > (depth + 1)): #checks to see if current index
                                                                                        #has been hit or if it has fewer
                                                                                        #moves to get to correct edge
                                                                                        #orientation than is currently
                                                                                        #there
                pruning_table[new_cube.edge_orientation_index()] = (depth + 1) #replaces the value with the new min
                                                                               #number of moves to get to a correct edge
                                                                               #orientation state
                queue.append((new_cube, depth + 1)) #appends new cube to end of queue. This is where the pruning occurs
                                                    #as cubes that do not pass the if statement do not get added meaning
                                                    #the branch gets cut off
    return pruning_table #returns the pruning table

def corner_pruning_table(objects, states):
    table_size = states ** objects

    pruning_table = [-1] * table_size

    solved_cube = RubiksCube()
    start_index = solved_cube.corner_orientation_index()
    pruning_table[start_index] = 0

    queue = deque()
    queue.append((solved_cube, 0))

    moves = ["r", "rprime", "rtwo",
             "l", "lprime", "ltwo",
             "f", "fprime", "ftwo",
             "u", "uprime", "utwo",
             "b", "bprime", "btwo",
             "d", "dprime", "dtwo"]

    while queue:
        cube, depth = queue.popleft()
        for move in moves:
            new_cube = copy.deepcopy(cube)
            getattr(new_cube, move)()
            if pruning_table[new_cube.corner_orientation_index()] == -1 or pruning_table[new_cube.corner_orientation_index()] > (depth + 1):
                pruning_table[new_cube.corner_orientation_index()] = (depth + 1)
                queue.append((new_cube, depth + 1))
    return pruning_table

def corner_edge_slice_pruning_table():
    rows = 3**7 #corner
    columns = 2**11 #edge

    pruning_table = [[-1 for i in range(columns)] for j in range(rows)]

    solved_cube = RubiksCube()
    edge_start_index = solved_cube.edge_slice_index()
    corner_start_index = solved_cube.corner_orientation_index()
    pruning_table[corner_start_index][edge_start_index] = 0

    queue = deque()
    queue.append((solved_cube, 0))

    moves = ["r", "rprime", "rtwo",
             "l", "lprime", "ltwo",
             "f", "fprime", "ftwo",
             "u", "uprime", "utwo",
             "b", "bprime", "btwo",
             "d", "dprime", "dtwo"]
    i = 0
    while queue:
        cube, depth = queue.popleft()
        for move in moves:
            new_cube = copy.deepcopy(cube)
            getattr(new_cube, move)()
            if pruning_table[new_cube.corner_orientation_index()][new_cube.edge_slice_index()] == -1 or pruning_table[new_cube.corner_orientation_index()][new_cube.edge_slice_index()] > (depth + 1):
                pruning_table[new_cube.corner_orientation_index()][new_cube.edge_slice_index()] = (depth + 1)
                queue.append((new_cube, depth + 1))
                i+=1
                print(i)
    np.savetxt("CornerEdgeSlicePruningTable", pruning_table, delimiter=",")
    return pruning_table


def checker():
    solved_cube = RubiksCube()
    queue = []
    queue.append((solved_cube, 0))
    moves = ["r", "rprime", "rtwo",
             "l", "lprime", "ltwo",
             "f", "fprime", "ftwo",
             "u", "uprime", "utwo",
             "b", "bprime", "btwo",
             "d", "dprime", "dtwo"]
    arr = []
    sum = 0
    while queue:
        cube, depth = queue.pop(0)
        for move in moves:
            new_cube = copy.deepcopy(cube)
            getattr(cube, move)()
            print(move)
            print("Depth = ",{depth})
            print(cube.edge_orientations)
            print("Index = ",{cube.edge_orientation_index()})
            arr.append(cube.edge_orientation_index())
            queue.append((new_cube, depth + 1))

def orient_edges(cube, edge_pruning_table):
    moves = ["r", "rprime", "rtwo", "l", "lprime", "ltwo",
             "f", "fprime", "ftwo", "u", "uprime", "utwo",
             "b", "bprime", "btwo", "d", "dprime", "dtwo"] #array of allowed moves on cube
    stack = [(cube, [])] #creates stack that takes in tuple of cubes and thier current path
    visited = set() #creates set of visited states
    while stack: #creates loop for when stack is no empty
        current_cube, path = stack.pop() #removes top cube on stack along with current path
        if current_cube.edge_orientation_index() == 0: #if cube is oriented correctly return the move path
            return path
        edge_current_state = current_cube.edge_orientation_index() #creates current edge state index
        if edge_current_state in visited: #if current state has been visited skip this loop
            continue
        visited.add(edge_current_state) #add current edge to visited edges
        for move in moves:
            new_cube = copy.deepcopy(current_cube) #creates copy of cube so future states are not messed up
            getattr(new_cube, move)() #applies current move to new cube
            new_cube_edge_index = new_cube.edge_orientation_index() #finds the new cube's index in pruning table based
                                                                    #off edge orientation
            if (edge_pruning_table[new_cube_edge_index] < edge_pruning_table[edge_current_state]
                    and edge_pruning_table[new_cube_edge_index] > -1): #checks to see if number of moves from old state
                                                                       #to new state decreases. If it does then adds
                                                                       #move to path and appends stack with new cube
                stack.append((new_cube, path + [move]))
    return [] #returns empty array if stack is empty and cube is not correctly oriented. Idicates an error as every cube
    #should return a path of moves as all are solvable

def state_checker(solution):
    print("Pre-Solution Orientation State: ",cube.edge_orientations())
    state_checker_cube = copy.deepcopy(cube)
    for move in solution:
        getattr(state_checker_cube, move)()
    print("Solution Orientation State: ",state_checker_cube.edge_orientations())
    state_checker_cube.print()

def state_implementor(solution):
    print("Pre-Solution Orientation State: ",cube.edge_orientations())
    for move in solution:
        getattr(cube, move)()
    print("Solution Orientation State: ",cube.edge_orientations())
    cube.print()


cube = RubiksCube()
cube.b()
cube.utwo()
cube.f()
cube.d()
cube.f()
cube.rprime()
cube.ftwo()
cube.b()

edge_pruning_table = edge_pruning_table(11, 2)
corner_pruning_table = corner_pruning_table(7, 3)

edges_are_oriented = orient_edges(cube, edge_pruning_table)
print("Phase 1 solution:", edges_are_oriented)

state_checker(edges_are_oriented)
state_implementor(edges_are_oriented)

print(cube.edge_in_slice())



print(corner_pruning_table)
print(edge_pruning_table)

sum = 0
for i in corner_pruning_table:
    if i == -1:
        sum +=1

print("Missed Inicies: ", sum)

print(corner_edge_slice_pruning_table())
