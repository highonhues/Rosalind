#variables and some arithmetic
#Problem
# Given: Two positive integers a and b, each less than 1000.

# Return: The integer corresponding to the square of the 
# hypotenuse of the right triangle whose legs have lengths a

#  and b
#bro my english is so bad it took me so long to comprehend

a = int(input("Enter number a:"))
b = int(input("Enter number b:"))

# use and for logical comparisons between boolean
if (0 < a < 1000) and (0 <b < 1000):
    h = a*a + b*b
    print(h)

# for rosalind
