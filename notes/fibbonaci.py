# Task 1
var1 = input("Please input your first number: ")
var2 = input("Please input your second number: ")

var1 = float(var1)
var2 = float(var2)


var4 = ((var1*var2) + (var1+var2) + (var1-var2) + (var1/var2))

print ("The sum is "+str(int(var4)))

if (var1 % var2 != 0):
    print ("The outputted value has a remainder of: " + str(var1 % var2))

"""
# Fibonnaci Numbers
arr = [0]

x = z = 0
y = 1

for x in range(16):
    a = y
    y = z
    z = a + y
    arr.append(z)

print(arr)
"""