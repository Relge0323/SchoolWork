from paintJob import PaintJob

# Author: Silvia Preston
# Filename: paintJob_obj.py
# Date: 11/05/24

# This program calculates the cost to paint a room
# given the room dimensions.

def hashtags():
    return "###############################################"

def displayHeader():
    ######### Display info #########
    print(hashtags())
    print("#  Welcome to the Paint Job Quote Calculator  #")
    print(hashtags())

def getValue(str):    
    valid = True
    while (valid):
        try:
            val = int(input("\t" + str + " >> "))
            valid = False
        except ValueError:
            print("***ERROR: Must enter an valid numeric value.***")

    return val

def getWindow():
    while(True):
        wind = input("Does the room have window(s), type y(yes) or n(no) >> ")
        if (wind.lower() != 'y' and wind.lower() != 'n'):
            print("***ERROR: must enter y or n only!***")
        else:
            break
    return wind.lower()

def printToFile(paintJob, paintJobObj):
    paintJob.write(f'\n{paintJobObj.getRoomName()} Dimensions:\n')
    paintJob.write(f'--------------------\n')
    paintJob.write(f'Length ........ {paintJobObj.getRoomL()}\n')
    paintJob.write(f'Width ......... {paintJobObj.getRoomW()}\n')
    paintJob.write(f'Height ........ {paintJobObj.getRoomH()}\n')
    paintJob.write('\n')     #write a blank line

    if (paintJobObj.getNumWindows() > 0):
        paintJob.write(f'The {paintJobObj.getRoomName()} has {paintJobObj.getNumWindows()} window(s)\n')
        paintJob.write(f'Total window area (in sqft).......................{paintJobObj.getWindowArea():>4}\n')
        paintJob.write(f'Total area minus the area of window(s) (in sqft)..{paintJobObj.getRoomArea():>4}\n')
    else:
        paintJob.write(f'Total {paintJobObj.getRoomName()} area (in sqft) {paintJobObj.getRoomArea():>7}\n')

    paintJob.write(f'\n\t\t\tCost totals for the {paintJobObj.getRoomName()}:\n')
    paintJob.write(f'\tMaterials.....................$ {paintJobObj.getMatCost():>10.2f}\n')
    paintJob.write(f'\tLabor.........................$ {paintJobObj.getLaborCost():>10.2f}\n')
    paintJob.write(f'\tCost total....................$ {paintJobObj.getTotalCost():>10.2f}\n')

def writeToExcel(paintJobObj):
    strtxt = 'Customer Name,' + paintJobObj.getCustomer()
    with open ('invoice.csv', 'w') as csv_file:
        csv_file.write(strtxt + "\n")
        csv_file.write("Room,Number of Windows,Area,Cost\n")
        for k, v in paintJobObj.getRoomDict().items():
            csv_file.write(k + ",")
            for val in v:
                strtxt = str(val) + ","
                csv_file.write(strtxt)
            csv_file.write("\n")

def main():
    grandTotal = 0

    displayHeader()
    
    #ask the user to enter the name of the input file
    fileName = input("\nTo get started, enter the name of the file to save the quote to >> ")
    # open a file 
    paintJob = open(fileName, 'w')   

    print("Enter the following information:")    
    # Ask for user input
    customer = input("\tWhat is the customer name >> ")

    #create a new paintJob instance object
    paintJobObj = PaintJob(customer)    
    numRooms = getValue("Number of rooms you want to paint")
    #set the number of rooms for the 
    paintJobObj.setNumRooms(numRooms)

    # go ahead and print the header of the document and the
    # name of the customer to the file.
    paintJob.write(hashtags())
    paintJob.write(f'\nPaint Job Quote Results\n')
    paintJob.write(hashtags())    
    paintJob.write(f'\nCustomer Name: {customer}')
    paintJob.write(f'\nNumber of rooms to paint: {numRooms} rooms')
    
    count = 0    
    while (count < numRooms):
        print(f'\nEnter information for room {count+1}:')

        room = input("\tWhat room is this (bedroom, kitchen, living room, etc) >> ")
        
        #set the room name for the paintJob object
        paintJobObj.setRoomName(room)

        #set the wall attributes
        paintJobObj.setRoomL(getValue("Length of the wall"))
        paintJobObj.setRoomW(getValue("Width of the wall"))
        paintJobObj.setRoomH(getValue("Height of the wall"))

        #ask if room has window
        hasWindow = getWindow()

        windowArea = 0  
        numWindow = 0      
        
        #if room has window
        if (hasWindow == "y"):
            #get the number of windows
            numWindow = getValue("Number of windows the " + room + " has")
            count_w = 1
            #calculate the area of each window in the room
            while (count_w <= numWindow):            
                w_len = getValue("Length of window " + str(count_w))
                w_height = getValue("Height of window " + str(count_w))
                paintJobObj.setWindowL(w_len)
                paintJobObj.setWindowH(w_height)                
                windowArea += w_len * w_height
                count_w += 1  #window count  
        
        #set the number of windows for the object
        #set window and room areas
        paintJobObj.setNumWindows(numWindow)
        paintJobObj.setWindowArea()                           
        paintJobObj.setRoomArea()

        totalCost = paintJobObj.getTotalCost()  
        #grandtotal holds the total for all rooms
        grandTotal += totalCost

        # create the dictionary and 
        # write info to the file       
        paintJobObj.setRoomDict()
        printToFile(paintJob, paintJobObj)        

        count += 1      # count holds the number of rooms from 0 to numRooms-1
        
        #write customer name and dictionary values to the Excel file
        writeToExcel(paintJobObj)

        #End of the while loop

    #Write the summary to the output file
    paintJob.write("\n****** Paint Job Summary ******\n")
    paintJob.write(str(paintJobObj))
    paintJob.write(f"\nGrand total for all rooms: ${grandTotal:.2f}")

    #Continue main    
    print(f"\nThank you for your input. Open the file {fileName} to view the quote.")

    # close the file
    paintJob.close()
    # end main

#call main
if __name__ == '__main__':
    main()