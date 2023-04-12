"""
Write a Python program that asks the user to enter a number and
then prints "Fizz" if the number is divisible by 3,
"Buzz" if the number is divisible by 5, and 
"FizzBuzz" if the number is divisible by both 3 and 5.
 If the number is not divisible by either 3 or 5,
 the program should just print the number.
"""

num=int(input("Enter the number:"))
if num%3==0 and num%5==0:
  print("FizzBuzz")
elif num%3==0:
  print("Fizz")
elif num%5==0:
  print("Buzz")
else:
  print(num)
 
