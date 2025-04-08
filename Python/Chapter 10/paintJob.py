"""
Author: Silvia Preston
File: paintJob.py
Description:

"""

class PaintJob():
    def __init__(self, customer):
        """Create a PaintJob instance object."""
        self.__customer = customer
        self.__labor = 3.00
        self.__gallon = 36.00
        self.__numRooms = 0
        self.__roomW = 0
        self.__roomL = 0
        self.__roomH = 0
        self.__roomName = ''
        self.__roomArea = 0
        self.__numWindows = 0
        self.__windowL = 0
        self.__windowH = 0
        self.__windowArea = 0
        self.__roomDict = {}
    
    #Set methods for class attributes
    def setCustomer(self, cust):
        self.__customer = cust

    def setLabor(self, labor):
        self.__labor = labor
    
    def setGallon(self, gallon):
        self.__gallon = gallon
    
    def setNumRooms(self, num):
        self.__numRooms = num
    
    def setRoomW(self, w):
        self.__roomW = w

    def setRoomL(self, l):
        self.__roomL = l

    def setRoomH(self, h):
        self.__roomH = h
    
    def setRoomName(self, name):
        self.__roomName = name

    def setRoomArea(self):
        # Area in square feet of a room with 4 walls = 2(L + W) * H 
        # Correct formula to calculate the surface area of a room:
        #  2(L * H) + 2(W * H)
        winArea = self.getWindowArea()
        if winArea > 0:
            self.__roomArea = (2*(self.__roomL * self.__roomH) + 
                               2*(self.__roomW * self.__roomH)) - winArea
        else:
            self.__roomArea =  2*(self.__roomL * self.__roomH) + 2*(self.__roomW * self.__roomH)

    def setNumWindows(self, numW):
        self.__numWindows = numW

    def setWindowL(self, l):
        self.__windowL = l

    def setWindowH(self, h):
        self.__windowH = h

    def setWindowArea(self):
        self.__windowArea = self.__windowL * self.__windowH

    def setRoomDict(self):
        self.__roomDict[self.__roomName] = [self.__numWindows, self.__roomArea, self.getTotalCost()]
    
    #Get methods for class attributes
    def getCustomer(self):
        return self.__customer
    
    def getLabor(self):
        return self.__labor
    
    def getGallon(self):
        return self.__gallon
    
    def getNumRooms(self):
        return self.__numRooms
    
    def getRoomW(self):
        return self.__roomW

    def getRoomL(self):
        return self.__roomL

    def getRoomH(self):
        return self.__roomH
    
    def getRoomName(self):
        return self.__roomName
    
    def getRoomArea(self):        
        return self.__roomArea
        
    def getNumWindows(self):
        return self.__numWindows
    
    def getWindowL(self):
        return self.__windowL

    def getWindowH(self):
        return self.__windowH
    
    def getWindowArea(self):
        return self.__windowArea
    
    def getRoomDict(self):        
        return self.__roomDict
    
    def getMatCost(self):    
        # 1 gallon paints 200 sq ft (if painting 2 coats; primer is included)
        # Gallons needed: area/200 sq ft
        galNeeded = self.getRoomArea()/200

        # Materials Cost: gallon price * gallons needed
        return self.__gallon * galNeeded

    def getLaborCost(self):
        # Labor cost = $3 * area in sq ft
        return self.__labor * self.getRoomArea()
    
    def getTotalCost(self):
        return self.getMatCost() + self.getLaborCost()

    def __str__(self):
        roomValues = str()
        roomValues += "Customer: " + self.__customer + "\n" + \
                      "Number of rooms: " + str(self.__numRooms) + "\n"
        for k, v in self.__roomDict.items():
            roomValues += "\n" + k + " Information:\n"
            roomValues += "\tNumber of Windows: " + str(v[0]) + "\n" \
                          "\t        Room Area: " + str(v[1]) + " sqrft\n" \
                          "\t       Total Cost: $" + str(v[2]) + "\n"
        
        return roomValues   

