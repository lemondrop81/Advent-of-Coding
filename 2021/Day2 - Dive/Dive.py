def start():

    # Getting the text input
    text_file = open("2021\Day2 - Dive\Day2.txt","r")
    lines = text_file.readlines()

    x = range(0, len(lines))

    # Adding to the running total of horizontal position
    horizontal = 0

    # Adding to the running total of depth position
    depth = 0

    # The for loop to iterate through every item
    for i in x:
        
        # Split the string up into movement and value
        j = lines[i].split(" ")
        

start()