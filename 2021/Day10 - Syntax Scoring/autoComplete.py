
text_file = open("2021\Day10 - Syntax Scoring\Day10.txt","r")
lines = text_file.readlines()

# opening and closing brackets
OPENING = ['(', '[', '{', '<']
CLOSING = [')', ']', '}', '>']

# Determine the error points
points = {")": 3, "]": 57, "}": 1197, ">": 25137}

# Determines the total of the scores
score = []

# Loop through all the input lines
for i in lines:
    found = []
    count = []
    error = False

    # Loop through each individual line to check if the brackets are the same
    for c in i:
        if c in OPENING:
            count.append(c)

        elif c in CLOSING and c == CLOSING[OPENING.index(count[-1])]:
            count.pop
        else:
            error = True
            break

# Print the sum of the scores
