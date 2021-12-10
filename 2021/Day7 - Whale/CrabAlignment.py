import statistics
data = list(map(int,open("2021\Day7 - Whale\Day7.txt").read().split(',')))

def start():
    # Calculate what the medium distance is
    medium = statistics.median(data)
    print(medium)
    fuel = 0

    for crab in data:
        print(crab)

start()