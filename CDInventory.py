#------------------------------------------#
# Title: CDInventory.py
# Desc: ADD,DEL,SAVE,LOAD CD DATA - Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# Muthu, 2021-Feb-12, Added Fuctionality to save data to file
# Muthu, 2021-Feb-13, Added Functionality  to load data from file to a table
# Muthu, 2021-Feb-14, Added Functionality to delete a record
#------------------------------------------#

# Declare variables


strChoice = '' # User input
dictTbl = []  # list of dictionaries to hold data
dictRow = {} # list of data row
strFileName='CDInvent.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('\nThe Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()
    
    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    
    if strChoice == 'l':
        # Added the functionality of loading existing data
        dictTbl=[]      
        # read the file line by line into in-memory dictionary 
        # keep adding by appending the dictionary to a list
        objFile=open(strFileName,'r')
        for row in objFile:
            lstRow=row.strip().split(',')
            dictRow={'CD ID':int(lstRow[0]), 'CD Title':lstRow[1],'Artist':lstRow[2]}
            dictTbl.append(dictRow)
        objFile.close()  
        print('Loaded from file successfully.\n Choose option i to view loaded data')
        pass

    if strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        lstRow = [intID, strTitle, strArtist]
        dictRow={'CD ID':intID,'CD Title':strTitle,'Artist':strArtist}
        dictTbl.append(dictRow)        
        pass
        
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID\t\t\t    CD Title\t\t\t  Artist')
        # Display from 2D list row by row
        for row in dictTbl:
            print(row)
        print('\n')    
        pass    
            
    elif strChoice == 'd':
        # deleting an entry when user gives CDID to delete
        ind=0 # to track the index of the list when record corresponding to CDID match
        flag=0  # to stop search when a matching record is found    
        strDel=input("Enter the CD ID to delete the corresponding entry\n")        
        for row in dictTbl:            
            item=row.get('CD ID')
            if str(item) != str(strDel):
                continue
            else:
                flag=1
                
        if flag==0:        
            print('No such Record exist\n')
        else:  
            for row in dictTbl:            
                item=row.get('CD ID')
                if str(item) == str(strDel):
                    print('Record to get deleted is\n')
                    print(row)
                    confirm=input('Do you confirm the operation? If so press C\n').lower()
                    if (confirm=='c'):
                        dictTbl.pop(ind)
                        print('record deleted')
                        break
                ind=ind+1               
        pass                
    
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile=open(strFileName,'w')
        for row in dictTbl:
            strRow=''
            for item in row.values():
                strRow=strRow+str(item)+','
            strRow=strRow[:-1]+'\n'   
            objFile.write(strRow)     
        objFile.close()
        print('Dictionaries saved to file successfully.\n')
        pass           
    
    else:
        print('Please choose either l, a, i, d, s or x!')

