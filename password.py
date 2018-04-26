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
    c = len(p)/4;

    ups = checkUpper(p);
    lows = checkLower(p);
    nums = checkNum(p);
    symbs = checkSymb(p);

    return math.fabs( len(ups)-c ) + math.fabs( len(lows)-c) + math.fabs(len(nums) - c ) + math.fabs( len(symbs) -c ) ;

print(rate("KELly"))
    
