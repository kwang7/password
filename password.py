#Kelly WANG
#SoftDev2 pd7
#K15 -- Do You Even List?
#2018-04-25

import math

UC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lc = "abcdefghijklmnopqrstuvwxyz"
num = "1234567890"
sym = ".?!&#,;:-_*"

def checkUpper(p):
    tot = [1 for x in p if x in UC]
    return tot

def checkLower(p):
    tot = [1 for x in p if x in lc]
    return tot

def checkNum(p):
    tot = [1 for x in p if x in num]
    return tot

def checkSymb(p):
    tot = [1 for x in p if x in sym]
    return tot

def superCheck(p):
    ups = checkUpper(p);
    lows = checkLower(p);
    nums = checkNum(p);

    return len(ups)>0 and len(lows)>0 and len(nums)>0

print (superCheck("Lo1"))
print (superCheck("KELY"))


def rate(p):
    c = len(p)/4.0;

    ups = checkUpper(p);
    lows = checkLower(p);
    nums = checkNum(p);
    symbs = checkSymb(p);

    #the lower the number the stronger the password is
    return (math.fabs( len(ups)-c ) + math.fabs( len(lows)-c) + math.fabs(len(nums) - c ) + math.fabs( len(symbs) -c )) /c ;

print(rate("KELlLLL14346Lada!!!!!sy"))
print(rate("KELLwang"))
print(rate("KL"))
print(rate("Ke2!"))
print(rate("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL"))

