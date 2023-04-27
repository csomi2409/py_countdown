import time                                         #Import time module

def countdown(t):                                   #Create a function which takes in the t parameter
    while t != 0:                               
        mins, secs = divmod(t, 60)                  #Divmod is a function which formates 2 separate numbers to 1 number
        
        timer = '{:02d}:{:02d}'.format(mins, secs)  #The '{:02d}:{:02d}' formats the time to 2 digits and .format assigns it to the variables
        
        print(timer, end="\r")                      #'\r' puts the cursor to the beginning of the line
        
        time.sleep(1)                               #Make the program wait one second 
        
        t -= 1                                      #Decreases the t value by one

    if t == 0:                                      #Finish in the end
        print("Finish")

    else:
        countdown(t)                                #Calls the function again

t = int(input("Enter the time in seconds:"))        #User inputs the amount of seconds

countdown(int(t))                                   #First call of the function