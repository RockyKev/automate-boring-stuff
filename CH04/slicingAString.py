

## FAIL
## Goal - replace 'a' with 'the
# name = 'Zophie a cat'
# name[7] = 'the'

## WORKING
## mutate and slicing
name = 'Zophie a cat'

newName = name[0:7] + 'the' + name[8:12]

print(name)
print(newName)
