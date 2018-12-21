
##tuples are just like lists
eggs = ('hello', 42, 0.5)

print(eggs[0])

## Unlike lists, tuples are immutable. 

#if you have one item in your tuple, add a comma.

bear = ('brown',) 

dog = ('black') 

## otherwise, they'll think it's a value.
print(bear[0])  ## gives brown
print(dog[0]) ## only gives b (for black)