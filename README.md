# AttainU Python Project
```
Project Name : Maze Solver 
Auther : Bhavleen Singh Manaktala 
Author Email : singhbhavleen3@gmail.com
```
[Question Link](https://docs.google.com/document/d/1reuKwhN8QLKJnqondL8vAnEvBFtexblLBgKJn1kT1N8/edit 'Maze Solver Problem')

## Maze Solver

The `Maze Solver` is a program that takes input as an NxN matrix and outputs the path of the maze denoting 1 as path and 0 as block/wall.

**This Read me file consits of following topics:**
- First step after opening **Python Project**. 
- How to run MazeSolver In Windows Operating System.
- How to run MazeSolver In Linux Operating System.
- My Approach to tackle the problem.
- Code Explanation (function by function).
- Modules used.
- My Final Words.

## First step after opening **Python Project**

Github Python Project consists of 3 contents.

1. README.md

2. mazeSolver.exe

3. mazeSolver.py

### README.md 
Is a User Manual for mazeSolver.py

### mazeSolver.exe
Installer of mazeSolver

### mazeSolver.py
Raw code of mazeSolver.py

## How to run MazeSolver In Windows Operating System

Firstly, in the `python project` directory you can see input.txt file give your maze combination to that file.

`Things to keep in mind while making a maze.`

The input should be space-separated like, `1 0 0 1 0 1 0` likewise.
>Don’t forget to give space between each numeral

Now, that you give input correctly. In the same directory, you can see W_MazeSolver.bat file just double click on that file and the program will automatically generate output.txt file with the correct path.

And in the case, you don't want to name output file as output.txt then in that case,

First, make .txt file type in the command

`mazeSolver (name_of_input_file.txt) (name_of_output_file.txt)`

then after editing change this file extension to .bat and run it by double-clicking the icon

## How to run MazeSolver In Linux Operating System

Firstly, in the `python project` directory you can see input.txt file give your maze combination to that file.

`Things to keep in mind while making a maze.`

The input should be space-separated like, `1 0 0 1 0 1 0` likewise.
>Don’t forget to give space between each numeral

Now, that you give input correctly. In the same directory, you can see L_MazeSolver.sh file just double click on that file and the program will automatically generate output.txt file with the correct path.

And in the case, you don't want to name output file as output.txt then in that case,

First, make .txt file type in the command

`python mazeSolver.py (name_of_input_file.txt) (name_of_output_file.txt)`

then after editing change this file extension to .sh and run it by double-clicking the icon

## My Approach to tackle the problem

My first approach is always to do this project by BFS because breadth-first search always gives the shortest path as the nature of its algorithm, I asked the instructor about it too but after ending the coding part successfully I noticed it taking a long time to just execute the code after wasted my couple of days to just optimized that code I realized this not gonna help me, that is where I opt for the recursion and backtracking part and realize that in terms of time complexity, these techniques are one step ahead of that algorithm to solve this problem.
And 1 coding standard which I remember while coding is `KISS`

>KEEP IT SIMPLE, STUPID

### Code Explanation (function by function)

Program is starting from line 49, where I'm asking the user to give input file and destination file name with the help of python module named as `argparse` .

Then on line 58, I'm taking maze as list and on line 59 to 61 taking user inputs and storing into maze list.

**authorize_maze() Function**

Firstly, making out_maze exact same format as given input maze, you can also call it a copy of user input maze but with all elements as 0, just a structure of user input maze.

If src (starting_point) is 0, then it will print(-1) i.e, Maze has no path.

If the path found between src(starting_point) and dest(destination_point) then it will be printed on output file where 0 blocks and 1 is the path walkover.

**maze_solver() Function**

If dest(destination_point) is 1 or not, if dest(destination_point) is 0, then it will print (-1) i.e, Maze has no path, then moving to authorize index step by step and after that recursion, starts and find the path.

**authorize_index() Function**

Basically, this function authorizes indices/format of the matrix


## Modules Used

In creating this program I used couple of predefined python modules like :

`argparse` - To get user input in command line

`pyinstaller` - To make .exe file 

## My Final Words

I've tried to implement all improvements suggested on the PEP 8 style guide to increase the readability of the code.

The function name in the program is direct that there is nothing to explain anything as the names of the functions are self-explanatory.

`THANK YOU`
