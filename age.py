"""Write a Python program that asks the user to enter their age
 and then prints "You are a minor" if their age is less than 18, 
"You are an adult" if their age is greater than or equal to 18 and less than 65, and
 "You are a senior" if their age is 65 or greater
"""

age=int(input("Enter the age:"))
if age<18:
  print("You are a minor.") 
elif age>=18 and age<65:
  print("You are an adult.")
else:
  print("You are a senior.")
