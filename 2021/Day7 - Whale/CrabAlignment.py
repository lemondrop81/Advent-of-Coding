import statistics
data = list(map(int,open("2021\Day7 - Whale\Day7.txt").read().split(',')))

def start():
    # Calculate what the medium distance is
    medium = round(statistics.median(data))
    fuel = 0

    # Loop through the crabs
    for crab in data:
       fuel += abs(crab - medium)

    # Print out the final value
    print(fuel)
start()