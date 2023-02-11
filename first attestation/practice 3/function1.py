import math, itertools

def gramsToOunces(grams):
    ounces = grams * 28.3495231
    return ounces

def fahToCen(fah):
    cen = (5/9) * (fah - 32)
    return cen

def howmany(numheads, numlegs):
    bunnum = (numlegs/2) - numheads
    chiknum = numheads - bunnum
    return bunnum, chiknum

# print(howmany(35,94))
# x = 3

def filter_prime(list:list):
    newlist = []
    for x in list:
        if x == 0 or x == 1:
            continue
        che = True
        for i in range(2, int(x/2)):
            if x%i == 0:
                che = False
        if che and x!=4:
            newlist.append(x)
    return newlist
# n = int(input())
# print(filter_prime([i for i in range(0, n)]))


def permutations_itertools(strings):
    return [''.join(p) for p in itertools.permutations(strings)]

print(permutations_itertools("abc"))

# print(permutation("abc"))


# for p in permutations("abc"):
#     print(p)


def strReverse(string):
    newlist = string.split(" ")
    newstring = ""
    for i in range(len(newlist)-1, -1, -1):
        newstring += (newlist[i])
        newstring += " "

    return newstring

def has_33(list):
    for i in range(len(list)-1):
        if list[i] == list[i+1] and list[i] == 3:
            return True
    return False

def spy_game(list):
    che = 0
    for i in list:
        if i == 0:
            che += 1
        if i == 7:
            che -= 2
            if che == 0:
                return True
    return False
# print(spy_game([0,1,0,2,7,2,4,5]))
def getV(r):
    return (4*math.pi*pow(r,3))/3

def getunique(list):
    i = 0
    while i < len(list):
        j = 0
        while j < len(list):
            if list[i] == list[j] and i!=j:
                list.pop(j)
            j += 1
        i = i + 1
    return list

def ispalindrom(string):
    left = string[0:int(len(string)/2)]
    right = string[int((len(string)+1)/2):len(string)]
    print(left[len(left)::-1], right)
    if left[len(left)::-1] == right:
        return True
    else:
        return False

def histogram(list):
    histo = ""
    for i in range(len(list)):
        if i == 0:
            histo += "*"*list[i]
        else:
            histo += "\n" + "*"*list[i]

    return histo

# print(histogram([3,4,5]))
print(filter_prime([x for x in range(1000)]))
