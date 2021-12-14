data = open("2021\Day14 - Polymerization\Day14.txt").read().split('\n')

def split(word):
    return [char for char in word]

t = split(data[0]) 
rules = []

# Loop through and split the rules up
for x in data:
     rules.append(x.split(' '))

# remove the first and last strings
rules.pop(0)
rules.pop(0)
rules.pop()

# Loop through the steps
for loopCount in range(10):
   
    # iterate through the pair insertion rules
    for rule in rules:

        # Initial value for the template loop
        i = 0

         # iterate through the polymer template
        while i < len(t) - 1:
            polymer = (t[i] + t[i+1])
            if rule[0] == polymer:
                # add the character to the middle of the list
                t = t[:1] + rule[2] + t[1:]

            i += 1