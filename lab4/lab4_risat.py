"""
Mahafog Risat
lab 4, dictionary and functions
September 10, 2025
"""
print("----- Example 1: dictionary -----")
# contact dictionary with three different users
contacts = {
    "Bill" : "718-111-2222",
    "Martha" : "646-000-3333",
    "Peter" : "212-000-1111"
}

print(contacts)

# Save the value of a specific key

user1 = contacts["Martha"]
print(f"user's phone number is {user1}")

# Add new content to the dictionary 

contacts["Anna"] = "646-222-3333"
print(contacts)

# Update value ofa specific key
contacts["Peter"] = "800-000-0000"
print(contacts)

print("----- Example 2: Loop through dictionary -----")
# print each key in the dictionary
for i in contacts:
    print(i)

# Print each value in the dictionary

for i in contacts:
    print(contacts[i])
    
# print each key:value set in the dictionary
    
for i in contacts:
    print(f"{i}: {contacts[i]}")

print("----- Example 3: length of a dictionary -----")
print(f"Dictionary has {len(contacts)} users")

print("----- Example 4: Copy a dictionary -----")
copy_contact1 = contacts.copy()
copy_contact2 = dict(contacts)

print(copy_contact1)
print(copy_contact2)

print("----- Example 5: Remove a key:value pair in a dictionary -----")
print(contacts)
contacts.pop("Peter")
print(contacts)

print("----- Example 6: Add a new key:value pair in a dictionary -----")
print(contacts)
contacts.update({"Lucas": "212-111-1111"})
print(contacts)

print("----- Example 7: Return items keys and values in a dictionary -----")
print(f"Returns itemss = {contacts.items()}")
print(f"Returns keys = {contacts.keys()}")
print(f"Returns values = {contacts.values()}")

print("----- Example 8: Dictionary application -----")
# store in a dictionary the count of occurency of the words in a phrase
phrase = "To be or not to be"
list_phrase = phrase.split()
# create an empty dictionary

word_count_dictionary = {}
for word in list_phrase:
    if word in word_count_dictionary:
        word_count_dictionary[word] += 1
    else:
        word_count_dictionary[word] = 1

# print result

for word in word_count_dictionary:
    print(f"'{word}' appears {word_count_dictionary[word]}")

print("----- EXERCISE -----")
users = ["peterpan@yahoo.com", "annie@hotmail.com", "Carl@hotmail.com", "martha@gmail.com", "cassie@yahoo.com", "Josue@hotmail.com", "John@hotmail.com"]

# create an empty dictionary

emails = {}

for email in users:
    email_type = email.split('@')[1].split('.')[0]
    if email_type in emails:
        emails[email_type] += 1
    else:
        emails[email_type] = 1
        
for email_type in emails:
    print(f"'{email_type}' appears {emails[email_type]}")