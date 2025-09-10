"""
    Mahafog Risat
    Lab 3, Python conditional statement and loops
    September 8th, 2025
"""

# condtional statement
print("\n ------ Example 1: if, elif,..., else -----")

"""
modify example 1
    - use while loop to validate if the user_number is between 1 and 9
    - user can only guess three times. This can be done using a for loop or a while
"""

#guess a number between 1 and 9
GUESS_NUM = 8

# collect the number
for attempts in range(3):
    user_number = int(input("Guess a number: "))
    # compare
    while user_number < 1 or user_number > 9:
        user_number = int(input("ERROR! Guess a number between 1 and 9: "))
    if(user_number == GUESS_NUM):
        print(f"Great Job! {user_number} is the guess mumber")
    elif (user_number > GUESS_NUM):
        print(f"{user_number} should be lower")
    elif (user_number < GUESS_NUM):
            print(f"{user_number} should be higher")
else:
    print("ERROR!")

print("End of guessing!")


print("\n ------ Example 2: control flow with logical operators -----")

# 'and', 'or', 'not' operators.
# 'and' operator returns TRUE only if all statements are true
# 'or' operator returns TRUE if at least one of the statement is true.
# 'not' operator returns the invert of the logic. TRUE --> not operator --> false

"""
    example 2: 
    - children under th age of 9 are only given milk for lunch
    - children between 10 to 14 are given a sandwich
    -children from 15 to 17 are given a burger
    
"""

age_student = int(input("Enter an age: "))
lunch = "None"
if age_student <= 9 and age_student >= 5:
    lunch = "milk"
elif age_student >= 10 and age_student <= 14:
    lunch = "sandwich"
elif age_student >= 15 and age_student <= 17:
    lunch = "burger"
else:
    lunch = "None"
    
print(f"At age {age_student} the food is {lunch}")

print("\n ------ Example 3: For loops -----")
# 'for' loop enables the program to execute a code block multiple times.
for n in range(2, 10):
    print(n)

print("\n ------ Example 4: For loops in a list -----")
years = [2011, 2005, 1998, 1980, 1973]
for y in years:
    print(y)
    
for index in range (len(years)):
    print(f"Year {index + 1} = {years[index]}")
    
print("\n ------ Example 5: While loops as a counter -----")
count = 1
while count <= 5:
    print(count)
    count += 1

print("\n ------ Example 6: While loops to validate a number -----")
# Validate if a number is between -5 and 5 (inclusive)

num = int(input("Enter a number between -5 and 5: "))

# use a while loop to recollect if the num is not between -5 and 5

while num < -5 or num > 5:
    num = int(input("ERROR! Enter a number between -5 and 5: "))
    
print(f"Entered number = {num}")
