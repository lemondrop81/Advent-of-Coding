
# Getting the text input
text_file = open("2021\Day10 - Syntax Scoring\Day10.txt","r")
lines = text_file.readlines()

# Determine the pairs
pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}

# Determine the error points
points = {")": 1, "]": 2, "}": 3, ">": 4}

# Determines the total of the scores
score = []

# Loop through all the input lines
for i in lines:
    found = []

    # Loop through each individual line
    for c in i:
        if c not in [")", "]", "}", ">"]:
            found.append(c)

        else:
            if c == pairs[found[-1]]:
                found.pop()

            else:
                score.append(points[c])
                found = []
                break


# Print the sum of the scores
print(sum(score))