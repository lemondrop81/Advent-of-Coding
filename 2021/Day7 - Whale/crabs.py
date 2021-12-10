import statistics
positions = list(map(int,open("2021\Day7 - Whale\Day7.txt").read().split(',')))

# precalculate cost of steps
steps=[0]
for i in range(1,1500):
    steps.append(steps[i-1]+i)

# choose a large number to compare the fuel cost to
final_fuel=99000000

aim_approx=round(statistics.mean(positions))

# Iterate through the range 
for aim in range(aim_approx-5, aim_approx+5):
    fuel=0
    # iterate through each of the crabs to find the fuel costs
    for position in positions:
        fuel+=steps[abs(position-aim)]
    if fuel<final_fuel:
        final_fuel = fuel

# Print the fuel costs
print(final_fuel)