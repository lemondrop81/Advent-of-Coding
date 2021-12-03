def start():

    # Getting the text input
    text_file = open("2021\Day3 - Binary Diagnostic\Day3.txt","r")
    lines = text_file.readlines()

    gamma = ""
    epsilon = ""

    for i in range(len(lines[0]) - 1):
        zeros = 0
        ones = 0

        for reading in range(len(lines)):
            print("test")


start()