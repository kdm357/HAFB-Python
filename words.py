"""
get a file from the web
http://icarus.cs.weber.edu/~hvalle/hafb/words.txt

task#1: count number of words in document
"""
from urllib.request import urlopen
file = "http://icarus.cs.weber.edu/~hvalle/hafb/words.txt"

count = 0
with urlopen(file) as story:
    for line in story:
        words = line.decode('utf-8').split()
        for word in words:
            count += 1
        print(count)

# Task #2
from urllib.request import urlopen
file = "http://icarus.cs.weber.edu/~hvalle/hafb/words.txt"
data = {}
count = 0
with urlopen(file) as story:
    for line in story:
        words = line.decode('utf-8').split()
        for word in words:
            if word in data:
                data[word] += 1
            else:
                data[word] = 1
    print(data)