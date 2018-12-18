## Practice Questions

## Q: 1. Why are functions advantageous to have in your programs?

Reusable code!

## Q: 2. When does the code in a function execute: when the function is defined or when the function is called?

When the function is called

## Q: 3. What statement creates a function?

def functioncodethingiename

## Q: 4. What is the difference between a function and a function call?

function is declaring it. 
function call is calling it. 

## Q: 5. How many global scopes are there in a Python program? How many local scopes?

There is one global scope. 
Local scopes are within the function, so it's as many as needed. 

## Q: 6. What happens to variables in a local scope when the function call returns?

The local scope variable is destroyed. 

## Q: 7. What is a return value? Can a return value be part of an expression?

return value is what happens after you call the function.

Expressions are composed of values and operators. 
An expression can be part of a return value. 

## Q: 8. If a function does not have a return statement, what is the return value of a call to that function?

None is returned. 

## Q: 9. How can you force a variable in a function to refer to the global variable?

by using the global statement. 
def spam():
    global eggs
    eggs = 'spam'

## Q: 10. What is the data type of None?

NoneType

## Q: 11. What does the import areallyourpetsnamederic statement do?

nothing. 

## Q: 12. If you had a function named bacon() in a module named spam, how would you call it after importing spam?

spam.bacon()

## Q: 13. How can you prevent a program from crashing when it gets an error?

using the try and except statements.


## Q: 14. What goes in the try clause? What goes in the except clause?

    try: 
        # what you want the software to happen
    except [whateverTheError]: 
        # result 