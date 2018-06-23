"""
Write a program to understand arithmatics in python
"""
# assignment operator
operand1 = 10
operand2 = 20

print("operands : %d , %d\n" % (operand1, operand2))

print("addition : %d " % (operand1 + operand2))
print("substraction : %d" % (operand1 - operand2))
print("multiplication : %d " % (operand1 * operand2))
print("division : %d " % (operand1 / operand2))

print("Explain the division result above ^\n\n\n")

print("division : %f " % (float(operand1) / float(operand2)))
print("division : %.2f " % (float(operand1) / float(operand2)))

print("5 power 2 ", (5 ** 2))

x = 132.5567/345.22

print("x : ", x)
print("rounding off values : ", round(x, 2))
