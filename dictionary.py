"""
learn dictionaries
dictionaries maps keys to values.

in some languages are known as asscoiative arrays, or hashs, maps

create then using {} containing a key-value pair
retrieve them by [key values]
"""

d = {'alice':'801-555-4452154',
     'pedro':'985-658-55874',
     'john':'9985-5587-885478'}
print(d, type(d))

#access an element
print(d['pedro'])

#add members to the dictionary, of names-> grades
roster = {} # empty dictionary
counter = 0
while counter < 3:
     name = input("Enter name:")
     grade = input("Enter Grade:")
     roster[name] = grade
     counter += 1
print(roster)