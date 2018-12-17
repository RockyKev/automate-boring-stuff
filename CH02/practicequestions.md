## Q:1. What are the two values of the Boolean data type? How do you write them?

True and False

must be written with capital letters

## Q:2. What are the three Boolean operators?

AND
OR
NOT

## Q:3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).

AND
true and true == True
true and false == False
false and true == False
false and false == False


OR

true or true == True
true or false == True
false or true == True
false or false == False


NOT
not True == False
not False == True

## Q:4. What do the following expressions evaluate to?

(5 > 4) and (3 == 5) == True && False == False
not (5 > 4) == !True == false
(5 > 4) or (3 == 5) == True || False == True
not ((5 > 4) or (3 == 5)) == !True || !False == False || True == True
(True and True) and (True == False) == False
(not False) or (not True) == !False || !True == True || False == True


## Q:5. What are the six comparison operators?

<
>
==

<=
>=
!

## Q:6. What is the difference between the equal to operator and the assignment operator?

= <---- assign this
== <---- compare this

## Q:7. Explain what a condition is and where you would use one.

Condition is what a loop needs to determine if something is true or not.

If you want a loop to run, it must meet the conditions.

## Q:8. Identify the three blocks in this code:


<!-- spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('spam') -->


spam = 0

if spam == 10:
    print('eggs')

    if spam > 5:
        print('bacon')
    else:
        print('ham')

    print('spam')

print('spam')


## Q:9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

spam = 40

if (spam == 1):
    print('Hello')
elif (spam == 2):
    print('Howdy')
else:
    print('Greetings!')

## Q:10. What can you press if your program is stuck in an infinite loop?

import sys

sys.exit()

## Q:11. What is the difference between break and continue?

break immediately kicks you out of a loop
continue... continues in the loop

## Q:12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?

range(10) <--- counts from 0 to 10
range (0, 10) <--- counts from 0 to 10, absolutely sure that it starts at those two values
range (0, 10, 1) <--- same, and absolustely sure it is counting by 1. 

## Q:13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

for i in range(11):
    print(i)

print("clear")

k = 0
while k < 11:
    print(k)
    k = k + 1


## Q:14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?

from bacon import *

## Extra credit: 
# Look up the round() and abs() functions on the Internet, and find out what they do. Experiment with them in the interactive shell.

round() == rounds the number

abs() == just gives the absolute value. 
So 20 == 20 
-20 == 20

