from collections import Counter

A, data = open("2021\Day14 - Polymerization\Day14.txt", 'r').read().split('\n\n')

def split(word):
    return [char for char in word]

t = split(data[0]) 
rules = []

# Loop through and split the rules up
for x in data.splitlines():
     i, j = x.split(' -> ')
     rules.append((i,j))

print(rules)

# Counts the number of times these occur
count = []

for step in range(10):
    insert = []
    for i in range(len(A)):
        for x in rules:
            if x[0] == A[i:i+2]:
                insert.append(x[1])
                break
    for i, x in enumerate(range(1, len(t)+len(insert), 2)):
        A = A[:x] + insert[i] + A[x:]


mostCommon = Counter(count).most_common
print(mostCommon)
