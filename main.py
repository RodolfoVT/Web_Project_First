import os
print(os.path.dirname(os.path.abspath(__file__)))

# Ask user for their name, name is the variable and input the function which helps us to already print out the question
# From there we are going to use the function print to finally answer back the user based on the variable it was entered
# A parameter is the declared variable in the function (here the function is "input" which will pass "name" as the var)
# An argument belong to the function or method, it is the actual value passed (which will be name entered by the user)

# Have in mind the possible solutions for the same challenge:
# Either you use +, either you call the variable itself when printing
# Also don't forget the space usage possible parameters like "sep=" & "end"
# Using escaping parameters provides more flexibility on the text you want to show \
# Remove whitespace from str & Capitalize user's whole name

name = input("What's your name? ").strip().title()

# Split user's name into first name and last name
first, last = name.split(" ")

# Say hello to user using just the first name (noticed we are leveraging the previous function)
print(f"Hello, {first}")

# int stands for integer, means numbers. str stands for string, means letters