# Getting the text input
fishInput = list(map(int,open("2021\Day6 - lanternfish\Day6.txt").read().split(',')))

# How many days
days = 80

# Creates the list to hold the end value
fishlist = []

# iterate through all the fish ages, to count
for i in range(1, 8):

    #Checks how many fish are of this age
    if i in fishInput:
        fishCounter = fishInput.count(i)
        fishlist.append(fishCounter)

    else:
        fishlist.append(0)

print(fishlist)

for day in range(days):
    print("test")
