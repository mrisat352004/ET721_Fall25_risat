"""
Mahafog Risat
Lab 7, accessing data in a file
October 15, 2025
"""

from lab7_function import*

testing()
print("\n ----- example 1: reading file -----")
read_data("lab7_data/phrases.txt")

print("\n ----- example 2: reading specific portion of a file -----")
read_up("lab7_data/phrases.txt")

print("\n ----- example 3: reading specific portion using readline -----")
read_readline("lab7_data/phrases.txt")

print("\n ----- example 4: reading specific portion using readline -----")
read_all("lab7_data/phrases.txt")

print("\n ----- example 5: loop through each line -----")
read_each("lab7_data/phrases.txt")

print("\n -----  example 6: creating a new file")
new_file("risat.txt")

print("\n -----  example 7: append data into existing file -----")
stamp_date("risat.txt")

print("\n ----- EXCERCISE -----")
count_yahoo = email_read("lab7_data/user_email.txt", "@yahoo")
count_gmail = email_read("lab7_data/user_email.txt", "@gmail")
count_hotmail = email_read("lab7_data/user_email.txt", "@hotmail")