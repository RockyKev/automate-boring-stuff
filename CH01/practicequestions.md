#Practice Questions

## Q: 1. Which of the following are operators, and which are values?


* <-- Operator
'hello' <-- Value
-88.8 <-- Value
- <-- Operator
/ <-- Operator
+ <-- Operator
5 <-- Value

## Q:2. Which of the following is a variable, and which is a string?


spam <-- Variable
'spam' <-- string

## Q:3. Name three data types.

RESPONSE: int, string, float

## Q:4. What is an expression made up of? What do all expressions do?

An expression is a programming instruction.
It's made with two actions. 

##Q: 5. This chapter introduced assignment statements, like spam = 10. What is the difference between an expression and a statement?

Expression is telling something to happen.
A statement is like your 'spam = 10' thing. 

## Q: 6. What does the variable bacon contain after the following code runs?

bacon = 20
bacon + 1

RESPONSE = bacon = 21

## Q: 7. What should the following two expressions evaluate to?

'spam' + 'spamspam'
'spam' * 3

RESULT: 
spamspamspam
spamspamspam

## Q: 8. Why is eggs a valid variable name while 100 is invalid?

100 starts with a number. 

## Q: 9. What three functions can be used to get the integer, floating-point number, or string version of a value?

int(var)
float(var)
str(var)


## Q: 10. Why does this expression cause an error? How can you fix it?

'I have eaten ' + 99 + ' burritos.'

99 is a integer. It would need to be converted to be a str.

I think 
print('I have eaten ' + str(99) + ' burritos.')
would work

##Extra credit: 
Search online for the Python documentation for the len() function. It will be on a web page titled “Built-in Functions.” Skim the list of other functions Python has, look up what the round() function does, and experiment with it in the interactive shell.

It rounds. 
Interestingly enough, it does have a tiny error based on decimal rounding.

> The behavior of round() for floats can be surprising: for example, round(2.675, 2) gives 2.67 instead of the expected 2.68. 