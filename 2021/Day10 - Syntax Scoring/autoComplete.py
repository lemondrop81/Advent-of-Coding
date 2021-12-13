
# Getting the text input
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

    # Loop through each individual line
    for c in i:
        if c in OPENING:
            


# Print the sum of the scores
print(sum(score))