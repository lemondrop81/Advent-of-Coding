
lines = [x.strip() for x in open("2021\Day10 - Syntax Scoring\Day10.txt", 'r').readlines()]

# opening and closing brackets
OPENING = ['(', '[', '{', '<']
CLOSING = [')', ']', '}', '>']

# Determines the total of the scores
score_list = []

# Loop through all the input lines
for i in lines:
    score = 0
    count = []
    error = False
    # Loop through each individual line to check if the brackets are the same
    for y in i:
        if y in OPENING:
            count.append(y)
        elif y in CLOSING and y == CLOSING[OPENING.index(count[-1])]:
            count.pop()
        else:
            error = True
            break
    # Manually set the value for the bracket
    if len(count) and not error:
        for z in count[::-1]:
            score *= 5
            if z == '(':
                score += 1
            elif z == '[':
                score += 2
            elif z == '{':
                score += 3
            elif z == '<':
                score += 4
        score_list.append(score)

# Print the scores
print(score_list)