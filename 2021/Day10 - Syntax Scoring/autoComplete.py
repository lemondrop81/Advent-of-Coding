
text_file = open("2021\Day10 - Syntax Scoring\Day10.txt","r")
lines = text_file.readlines()

# opening and closing brackets
OPENING = ['(', '[', '{', '<']
CLOSING = [')', ']', '}', '>']

# Determines the total of the scores
score = []

# Loop through all the input lines
for i in lines:
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

    if len(count) and not error:
        for z in count[::-1]:
            # Times the score by 5
            score *= 5

            if z == '(':
                score += 1
            elif z == '[':
                score += 2
            elif z == '{':
                score += 3
            elif z == '<':
                score += 4
        

# Print the sum of the scores
