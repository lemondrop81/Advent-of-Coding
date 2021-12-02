def start():

    # Getting the text input
    text_file = open("2021\Day1 - Sonar Sweep\Day1.txt","r")
    depths = list(map(int, text_file.readlines()))

    i = range(0, len(depths))
    
    # Adding to the running total of larger numbers
    total = 0
    
start()