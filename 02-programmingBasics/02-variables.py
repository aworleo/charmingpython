# write a program to show the behaviour of variables in python

"""
Variables are Storage containers. they provide space to store data
"""

# formatting a string with variable
var1 = 20
print("printing variable : ", var1)
print("the variable has %d value " % var1)

var1 = 10

print("the value of variable has been reassigned to : ", var1)

var2 = 30

# populating output with expressions
print("simple arithmatic with variables : ")
print("\tAddition : ", (var1 + var2))
print("\tSubstraction : ", (var1 - var2))
print("\tMultiplication : ", (var1 * var2))
print("\tDivision : ", (var1 / var2))

VAR1 = 33
# variables are case sensitive
print("case sensitive variable names : %d -- %d " % (var1, VAR1))
print ("printing variable : ", var1)
print ("the variable has %d value " % var1)

var1 = 10
print ("The value of variable has been reassigned to : ", var1)