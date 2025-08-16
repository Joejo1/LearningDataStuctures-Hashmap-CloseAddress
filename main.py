import numpy as np 
import pandas as pd
import csv

emptyValue = '......'

fl = np.array(pd.read_csv("name6000.csv"))
numOfNames = len(fl)
ar = np.array([[emptyValue] * 5 ] * (numOfNames * 2))
lenAr = len(ar)
arColl = np.array([[emptyValue] * 2] * (numOfNames * 2))
print(len(arColl))

print('Number of Keys:', numOfNames)

def hashKeys(lenAr, key):
    index = hash(key) % lenAr
    return index

def isCollision(arr, index):
    if arr[index][0] == emptyValue:
        return False
    else:
        return True

def setKeyInAr(arr, index, key):
    arr[index][0] = key
    return arr


CollisionNum = 0
numOfColl = 0
j = 0
for i in fl:
    key = fl[j][0]
    index = hashKeys(lenAr, key)
    isColl = False
    isColl = isCollision(ar, index)
    offSet = -1

    while isColl == True:
        offSet = offSet + 1
        isColl = isCollision(arColl, offSet)
        numOfColl = numOfColl + 1
    if offSet > -1:
        arColl = setKeyInAr(arColl, offSet, key)
        CollisionNum = CollisionNum + 1
    else:
        ar = setKeyInAr(ar, index, key)
    j = j + 1

emty = 0
full = 0
l = 0
for k in arColl:
    if arColl[l][0] == emptyValue:
        emty = emty + 1
    else:
        full = full + 1

    l = l + 1


print('Populated:', full, 'Empty:', emty)

print("num of coll:", numOfColl, "Number in second array:", CollisionNum)
print(ar)
print(arColl)
