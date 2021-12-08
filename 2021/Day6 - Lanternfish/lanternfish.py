# Getting the text input
def get_input():
    with open("2021\Day6 - lanternfish\Day6.txt", 'r') as f:
        data = [i for i in f]
    return [int(i) for i in data[0].split(',')]

days = 80
   

get_input()