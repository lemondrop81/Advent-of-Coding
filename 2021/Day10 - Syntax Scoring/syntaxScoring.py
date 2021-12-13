def start():

    # Getting the text input
    text_file = open("2021\Day10 - Syntax Scoring\Day10.txt","r")
    lines = text_file.readlines()
    
    # Determine the pairs
    pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}

    # Determine the error points
    points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    
    # Loop through all the input lines
    for i in lines:
        score = 0
        found = []

        # Loop through each individual line
        for c in i:
            if c not in [")", "]", "}", ">"]:
                found.append(c)


start()