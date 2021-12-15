from collections import Counter

A, data = open("2021\Day14 - Polymerization\Day14.txt", 'r').read().split('\n\n')

rules = []

# Loop through and split the rules up
for x in data.splitlines():
     i, j = x.split(' -> ')
     rules.append((i,j))

# Counts the number of times these occur
count = []

# Loops a certain number of times
for step in range(10):
    insert = []

    # Loop through the polymer
    for i in range(len(A)):

        # Loops through the rules, compared to the polymer
        for x in rules:
            if x[0] == A[i:i+2]:
                insert.append(x[1])
                break
    # Loops and inserts into the polymer
    for i, x in enumerate(range(1, len(A)+len(insert), 2)):
        A = A[:x] + insert[i] + A[x:]


count = Counter(A)
# print the output
print(count.most_common()[0][1] - count.most_common()[-1][1])
