#!/usr/bin/env python3
# Student ID: epatel16

def function1():
    # Do not modify the global schoolName here, just use it
    global schoolName
    schoolName = 'SICT'  # This will change the global schoolName to 'SICT'
    print('print() in function1 on schoolName:', schoolName)

def function2():
    global schoolName
    schoolName = 'SSDO'  # This will modify the global schoolName
    print('print() in function2 on schoolName:', schoolName)

# Global 'schoolName' variable initially set to 'Seneca'
schoolName = 'Seneca'
print('print() in main on schoolName:', schoolName)

# Call function1 (will modify the global schoolName to 'SICT')
function1()
print('print() in main on schoolName:', schoolName)

# Call function2 (will modify the global schoolName to 'SSDO')
function2()
print('print() in main on schoolName:', schoolName)

