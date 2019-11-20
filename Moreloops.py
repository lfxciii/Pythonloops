# Introduction to Programming, Task 15
# Ruben Louw, [2019-04-13]
# checks if any number supplied is a prime number or not

# Create a program to check if a number inputted by the user is prime.
# A prime number is a positive integer greater than 1, whose only factors are 1 and the number itself.
# Examples of prime numbers are: 2, 3, 5, 7, etc.
# Ask the user to enter an integer.
num = int(input("Please enter a number: "))

# First check if the number is greater than 1.
if num > 1:
   # If it is greater than 1, check to see if it has any factors besides one and itself.
   # i.e if there are any numbers between 2 and the number itself that can divide the number without any remainders 
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")           
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")





