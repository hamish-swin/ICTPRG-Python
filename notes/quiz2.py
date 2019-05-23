# Write the function between the START and END tags
# START
def IsPalindrome(pal):
    pal = pal.lower().replace(" ","")
    palRev = []

    for x in range(0, (len(pal))):
        palRev.append(pal[(len(pal) - (x+1))])

    if ''.join(palRev) == pal:
        return True
    
    return False
# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(IsPalindrome("GlenElg") == True))
print("Test 2 Passed: " + str(IsPalindrome("Nurses Run") == True))
print("Test 3 Passed: " + str(IsPalindrome("Nurses") == False))
print("Test 4 Passed: " + str(IsPalindrome("frank") == False))