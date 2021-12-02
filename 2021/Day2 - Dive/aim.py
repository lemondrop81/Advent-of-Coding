def start():

    # Getting the text input
    text_file = open("2021\Day2 - Dive\Day2.txt","r")
    lines = text_file.readlines()

    x = range(0, len(lines))

    # Adding to the running total of horizontal position
    horizontal = 0

    # Adding to the running total of depth position
    depth = 0

    #Add the running total for aim
    aim = 0

    # The for loop to iterate through every item
    for i in x:
        
        # Split the string up into movement and value
        j = lines[i].split(" ")

        # Checks to see if movement it forward
        if j[0] == "forward":
            # Goes forward certain amount
            horizontal += int(j[1])
            depth = aim * int(j[1])
        
        # Checks to see if movement is down
        elif j[0] == "down":
            # increases depth when submarine goes down
            depth += int(j[1])
            aim += int(j[1])
        
        # Checks to see if movement is up
        elif j[0] == "up":
            # subtracts depth when submarine goes up
            depth -= int(j[1])
            aim -= int(j[1])


start()