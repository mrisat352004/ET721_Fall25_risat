"""
Mahafog Risat
function file
September 16, 2025
lab 5, functions
"""

# Example 1: define a function that passes two numbers and return the product of it
def product(a=0,b=0):
    c = a*b
    return c

# Example 2: function to calculate the hypotenuse
def hypotenuse(s1, s2):
    return (s1**2+s2**2)**0.5

# Example 3: function to check if the number is positive, negative, or zero.
# the function returns a string
def check_number(num):
    if(num>0):
        return "POSITIVE"
    elif (num<0):
        return "NEGATIVE"
    else:
        return "ZERO"
    
# Example 4: function to calculate the average of a list of grades, and return 'true' if the average is greater than 60, otherwise, it returns 'false'

def check_grades(grades):
    # initialize the average grade value
    avg = 0
    # sum the individual 'g' from list 'grades' into 'avg'
    for g in grades:
        avg += g
    # find the average grade
    avg /= len(grades)
    return avg

def check_pass(avg_grade):
    # check if the average is greater than 60
    if avg_grade >= 60:
        return True
    else:
        return False

# EXERCISE
def guess_number(random):
    guess = 10
    if random < guess:
        return print("The number is smaller than the guess number")
    elif random > guess:
        return print("The number is bigger than the guess number")
    else:
        return print("You got it!")