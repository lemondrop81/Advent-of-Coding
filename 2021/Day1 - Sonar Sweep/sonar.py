def start():
    values = [1, 2, 1, 4, 5]

    text_file = open("2021\Day1 - Sonar Sweep\Day1.txt","r")

    i = range(0, len(values))
    
    total = 0

    for x in i:
        if x < max(i):
            if values[x] < values[x+1]:
                print("larger")

                total += 1

            else:
                print("smaller")

    print(total)
start()