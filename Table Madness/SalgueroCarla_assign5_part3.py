'''
Carla Salguero

Help Craig Kapp gave in class: 
for i in range (10): #0-9
    print (format(i, ">4d"), end="")
print ()
# numbers along the left for j in range 10
for j in range (10): #0-9
    print (j, end="")
    #print the multiplicaiton row
    for k in range (0,10):
        print (format(j*k, ">4d"), end="")
    print()

'''
#Part 3: Table Madness


#Here just sets up the first few print statements. 
print ("Instructions: Choose which table you would like to build.")
print("Then enter the number of rows and columns that you would.")
print ("like present in the selected table.")
print()
print ("	1. Addition Table")
print ("	2. Subtraction Table")
print ("	3. Multiplication Table")
print ()
while True: #this starts off the while loop to insure that the user inputs either 1, 2, or 3. 
    table = int(input("Which table would you like to work with?: "))
    if table !=1 and table !=2 and table !=3: #This creates a limit on what is considered a valid number. 
        print ("Invalid table type, try again.")
    else:
        break #if the user inputs a valid number, then we can continue. 
print()
while True: #this starts the while loop to validate the number of rows
    rows = int(input("Enter # of rows: "))
    if rows <0:#rows have to be greater than 0! 
        print ("Invalid # of rows, try again. ")
    else:
        break #once this is validated, yay its done. 
while True: #this starts the while loop to validate the number of columns
    columns = int(input("Enter # of columns: "))
    if columns <0: #columns need to be greater than 0!
        print ("Invalid # of columns: ")
    else:
        break #once this is validated, yay its done. 

if table ==3: #I created this if statement specifically for multiplication table.   
    print("    * |", end="") #this sets up the chart. 
    for i in range (columns): # the loop will start with the columns. 
        print (format(i, ">9d"), end="") #i used 9 so if we have large numbers, there is room :)
    print ()
    print ("-"*(columns*11)) #this is used to separate what is being multiplied with eachother. 
    # numbers along the left for j in range 10
    for j in range (rows): #0-9
        if j < 10: #this checks the rows so that if there is any double digits, all lines will be allgined. 
            print ("   ",  j, "|", end="")
        else:
            print("   ", str(j) + "|", end="") #this is for numbers of one digits. 
        #print the multiplicaiton row
        for k in range (0,columns):
            print (format(j*k, ">9d"), end="") #this is the actual answer for the product. 
        print()
        
if table ==1: #I created this if statement specifically for addition table.
    print("     +|", end="") #this sets up the chart. 
    for i in range (columns): # the loop will start with the columns.
        print (format(i,">9d"), end="") #i used 9 so if we have large numbers, there is room :)
    print ()
    print ("-"*(columns*11))#this is used to separate what is being added with eachother. 
    # numbers along the left for j in range 10
    for j in range (rows): #0-9
        if j < 10: #this checks the rows so that if there is any double digits, all lines will be allgined.
            print ("   ",  j, "|", end="")
        else:
            print("   ", str(j) + "|", end="") #this is for numbers of one digits. 

        for k in range (0,columns):
            print (format(j+k, ">9d"), end="")#this is the actual answer for the addition. 
        print()
        
if table == 2: #I created this if statement specifically for subtraction table.
    print("     -|", end="")
    for i in range (columns): 
        print (format(i,">9d"), end="") #ISSUE HERE! ( WITH | and spacing of top row of numbers) 
    print()
    print ("-"*(columns*11)) #this is used to separate what is being subtraction from eachother.
    # numbers along the left for j in range 10
    for j in range (rows): #0-9
        if j < 10: #this checks the rows so that if there is any double digits, all lines will be allgined.
            print ("   ",  j, "|", end="")
        else:
            print("   ", str(j) + "|", end="") #this is for numbers of one digits. 

        for k in range (0,columns):
            print (format(k-j, ">9d"), end="") #this is the actual answer for the subtraction.
        print() 

