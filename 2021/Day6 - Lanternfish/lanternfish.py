# Getting the text input
data = list(map(int,open("2021\Day6 - lanternfish\Day6.txt").read().split(',')))

# Initialize the dictionary
data_dict = {}

# Populate the dictionary
for i in range(9):
    data_dict[i] = 0
    
data_dict["6_new"] = 0

# Loop through the number of fish    
for fish in data:
    data_dict[fish] += 1

def update_dict(data_dict):
    new_dict = {}

    new_dict[6] = data_dict[0]
    new_dict['6_new'] = data_dict[7]
    new_dict[5] = data_dict[6] + data_dict['6_new']

    for i in [1, 2, 3, 4, 5, 8]:
        new_dict[i-1] = data_dict[i]

    new_dict[8] = new_dict[6]
    
    return new_dict

# initialize the number of days
days = 80

for day in range(0, days):
    data_dict = update_dict(data_dict)

print(f"After {day+1} days: {sum(data_dict.values())} laternfishes.")

