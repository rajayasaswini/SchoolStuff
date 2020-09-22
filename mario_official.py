def makesteps(no):
    #assign 2 to the variable nohash
    nohash = 2
    #while the variable 'no' is more than 0
    while no > 0:
        #for loop to make pyramid
        for i in range(no):
            #prints each line with spaces and hashtags
            print(no*" "+nohash*"#")
            #everytime the program goes through the for loop, no
            #is decreased by 1 and nohash increases by 1
            no += -1
            nohash += 1

#asks user to input
height = int(input("Enter a number between 0 and 23: "))

#if the height isn't between 0 and 23, the user is asked again to input
while height<0 or height>23:
    height = int(input("Enter a number between 0 and 23: "))
#calls the function
makesteps(height)
