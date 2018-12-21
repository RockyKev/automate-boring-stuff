## Methods are similar to functions, but they're called ON a value. 

spam = ['hello', 'hi', 'howdy', 'heyas']

print(spam.index('hello')) ## 0

spam.append('wassup')

print(spam)

##Appends adds at the end

spam.insert(1, 'Yo')

print(spam)

##Insert adds it in the beginning

del spam[5]
print("del statement: - remove [5]")
print(spam)
## great for deleting with indexing

spam.remove("heyas")
## great for deleting with value
print("remove method: - remove heyas")
print(spam)
