# Write the function between the START and END tags
# START
"""
def MultiplyElementsInList(num):
    for y in num:
        out *= 
"""

def MultiplyElementsInList(x):
    out = 1
    for i in range(0, len(x)):
        out *= x[i]
    print(out)
    return(out)

# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(MultiplyElementsInList([1, 2, 3]) == 6))
print("Test 2 Passed: " + str(MultiplyElementsInList([0, 2, 3]) == 0))
print("Test 3 Passed: " + str(MultiplyElementsInList([2, 2, 2]) == 8))
print("Test 4 Passed: " + str(MultiplyElementsInList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 3041409320171337804361260816606476884437764156896051200000000000))