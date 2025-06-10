"""
Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.
"""

if __name__ == '__main__':
    odd =  even = 0
    
    n = int(input("Write a number: \t"))
    
    if n % 2 == 0:
        even = n
    else: 
        odd = n
        
    if n == odd:
        print("Weird")
    elif n == even and n >=2 and n <= 5:
        print("Not Weird")
    elif n == even and n >= 6 and n <= 20:
        print("Weird")
    elif n == even > 20:
        print("Not Weird")