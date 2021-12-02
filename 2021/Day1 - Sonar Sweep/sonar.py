def start():
    values = [1, 2, 1, 4, 5]

    # Getting the text input
    text_file = open("2021\Day1 - Sonar Sweep\Day1.txt","r")
    depths = list(map(int, text_file.readlines()))

    i = range(0, len(depths))
    
    # Adding to the running total of larger numbers
    total = 0

    # The for loop to iterate through every item
    for x in i:

        # Making sure the loop doesn't go past the end
        if x < max(i):

            #Checks to see if the value is larger then the previous one
            if depths[x] < depths[x+1]:

                total += 1
    
    #Print the total number
    print(total)
start()