try:  
    a = int(input("Enter a:"))    
    b = int(input("Enter b:"))    
    c = a/b  
except:  
    print("Can't divide with zero")  
else:
    print("HI chutiya")

print("another example of IOError:")

try:    
    #this will throw an exception if the file doesn't exist.     
    fileptr = open("file.txt","r")    
except IOError:    
    print("File not found")  
    print(IOError)  
else:    
    print("The file opened successfully")    
    fileptr.close() 
