#An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is equal to the number itself.
n = int(input("Enter the number to check wheather number is armstrong or not?!! "))
temp = n
z = 0
while (n>0):
    x = n%10
    x = x**3
    z = z+x
    n = n//10
if (z == temp):
    print("Given number is armstrong.")
else:
    print("Given number is not a armstrong number.")