def start():
    values = [1, 2, 1, 4, 5]

    for x in values:
        if values[x] < values[x-1]:
            print("smaller")
        else:
            print("larger")

start()