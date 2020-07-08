import argparse


def authorize_maze(maze):
    # copy of maze with all values as 0
    out_maze = [[0]*length for i in range(length)]

    # make sure source is (0,0)
    if maze[0][0] == 0 or maze[length-1][length-1] == 0:
        file1.write('-1')
        return False

    if maze_solver(maze, 0, 0, out_maze) is False:
        file1.write('-1')
        return False

    for i in out_maze:
        for j in i:
            file1.write(f' {str(j)} ')
        file1.write('\n')
    return True


def maze_solver(maze, x, y, out_maze):

    if x == length - 1 and y == length - 1:
        out_maze[x][y] = 1
        return True

    if authorize_index(maze, x, y) is True:
        out_maze[x][y] = 1

        if maze_solver(maze, x + 1, y, out_maze) is True:
            return True
        if maze_solver(maze, x, y + 1, out_maze) is True:
            return True
        out_maze[x][y] = 0
        return False

# checking if move is out Of matrix or not


def authorize_index(maze, x, y):

    if x >= 0 and x < length and y >= 0 and y < length and maze[x][y] == 1:
        return True

    return False  # if any index is -1 or in not proper format


# Real Game
pars = argparse.ArgumentParser()
pars.add_argument('ip_file', help='Input File')
pars.add_argument('op_file', help='Output File')
arg = pars.parse_args()

file = open(arg.ip_file, 'r')
file1 = open(arg.op_file, 'w')

# getting input from output file
maze = []
for data in file:
    [l.strip('\n') for l in data]
    maze.append([int(x) for x in data.split()])

length = len(maze)
authorize_maze(maze)
