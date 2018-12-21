# Say you have a list value like this:

# spam = ['apples', 'bananas', 'tofu', 'cats']

# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it.

spam = ['apples', 'bananas', 'tofu', 'cats']

weather = ['sunny', 'rainy', 'cold', 'hot', 'fog', 'snowy']

def CommaCode (listValue):

    newString = listValue[0] 

    for i in range(1, len(listValue)):
        newString = newString + ", " + listValue[i]
    
    return newString

print(CommaCode(spam))

print(CommaCode(weather))
