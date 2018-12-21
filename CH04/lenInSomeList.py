## common technique is using len

catList = ["gogo", "jojo", "stinky"]

for i in range(len(catList)):
    print("Index: " + str(i) + " and it represents " + catList[i])

## Check to see if things are IN the list
print('gogo' in catList) ##true

print('soki' in catList) ## false

## Check to see if things are NOT in the list.
print('soki' not in catList) ## true