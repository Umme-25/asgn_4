# asgn_4  -> Assignment 4

Task 1

    using 'try' block -> code executed when the file existed
        Opening the file with 'with' statement in reading mode.
        
        Using For loop -> 
             to read and write line one by one from the file.
             
     except block is executed 
           when the file does not exist ->FileNotFoundError 
    Display output accordingly.


Task 2

    Tking input from user and stored in 'data1'
    opening file with 'with' statement in 'write' mode so we can add the data without previous data
    after successfully writing to file we take next data to append
    
    now again opening file as before but using 'append' mode so that the preious added data is still inside file and should not be deleted.
    appended data is stored in 'data2' 
    after successfully adding dats2 to file
    
    now openning file to read the data from file 
    print -> data1 + data2  line by line
