# Conditions and loops
# Given: Two positive integers a and b
#  (a<b<10000)
# Return: The sum of all odd integers from a through b , inclusively.

a =int(input("a:"))
b=int(input("b: "))

if (a < b < 10000):
    z = 0
    for i in range(a,b+1):
      if (i %2 != 0):
         z +=i
         
    print(z)