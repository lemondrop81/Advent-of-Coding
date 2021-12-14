data = open("2021\Day14 - Polymerization\Day14.txt").read().split('\n')

def split(word):
    return [char for char in word]

for x in data:
    y = x.split('->')
t = split(data[0]) 

# Initial value for the template loop
i = 0

# iterate through the polymer template
while i < len(t) - 1:
    print(t[i] + t[i+1])
    i += 1