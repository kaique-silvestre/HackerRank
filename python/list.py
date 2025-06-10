"""
Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.

Example




All permutations of  are:
.

Print an array of the elements that do not sum to .


Input Format

Four integers  and , each on a separate line.

Constraints

Print the list in lexicographic increasing order.
"""
x = int(input('x '))
y = int(input('y '))
z = int(input('z '))
n = int(input('n '))
    
var = [[[x for x in range(y)] for y  in range(z)] for z in range(n)]

print(var)