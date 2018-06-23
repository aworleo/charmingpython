# write a program to print simple string
print("simple program to print a string")

# write a program to use format specifiers
print ("First Line \n Second Line at next position.")
print ("use of \t : tab")

# write a program to print a variable
paramValue = 20

# For details, refer "print style formatting" [https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting ]
print ("Printing Variable: %d" %paramValue)  # integer
print ("Printing Variable: %s" %paramValue)  # string
print ("Printing Variable: %f" %paramValue)  # float
print ("Printing Variable: %.3f" %paramValue)# float with decimal digits set by user
print ("Printing Variable: %g" % paramValue) # float

#write a program to print a paragraph. (multi line printing)
print ("\nMulti line printing")
print ("""
This is the way to print strings that are formatted in code
    -- avoids tabs
    -- avoids next lines
""")

complexPrint = ('Put several strings within parentheses''to have them joined together.')

print (complexPrint)

# using format string as a variable : 
formatter = ("%d.%d.%d.%d")
print ("\nIP address is:" + formatter %(192, 168, 0, 100))
