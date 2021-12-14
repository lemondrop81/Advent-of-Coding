data = open("2021\Day14 - Polymerization\Day14.txt").read().split('\n')

def split(word):
    return [char for char in word]

t = split(data[0]) 

for x in data:
    y = x.split(' ')


# Loop through the steps
for loopCount in range(10):

    # Initial value for the template loop
    i = 0
    # iterate through the polymer template
    while i < len(t) - 1:
        #print(t[i] + t[i+1])
        i += 1