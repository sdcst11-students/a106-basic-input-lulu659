#! python3
"""
Ask the user for their name and their email address.
(2 points)

Inputs:
 name
 email

Sample output:
 Your name is Joe Lunchbox, and your email is joe@koolsandwiches.org.

example:
What is your name:Dwayne Johnson
What ir your email:rock@aol.com

Your name is Dwayne Johnson, and your email is rock@aol.com

What is your name:Jackie Chan
What ir your email:crazyAsian@qq.com

Your name is Jackie Chan, and your email is crazyAsian@qq.com

"""

data = input ("What is your name? ")
print("You entered: " + data)
print("\n\n\n\n")
question = "What is your email?"
response = input(question)
print(f"Your email is {response}")
print("\n\n\n")
print(f"Your name is {data}, and your email is {response}")