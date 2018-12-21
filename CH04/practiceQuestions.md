
## Q:1. What is []?

creates a list. 
I want to say array, but that's different.

## Q:2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)

spam[2] = 'hello


------
For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].

## Q:3. What does spam[int(int('3' * 2) // 11)] evaluate to?

6 // 11 == 0
> // <-- Floor division - division that results into whole number adjusted to the left in the number line

so it's spam[0]

## Q:4. What does spam[-1] evaluate to?

d

## Q:5. What does spam[:2] evaluate to?

a,b

-------
For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].

## Q:6. What does bacon.index('cat') evaluate to?

1 - 
since it'll find the index of 'cat', and the first index of cat. 


## Q:7. What does bacon.append(99) make the list value in bacon look like?

[3.14, 'cat', 11, 'cat', True, 99]

## Q:8. What does bacon.remove('cat') make the list value in bacon look like?

[3.14, 11, 'cat', True]

## Q:9. What are the operators for list concatenation and list replication?

+ to add them to gether
[1, 2, 3] + [1, 2, 3] == [1, 2, 3, 1, 2, 3]

* to replicate it
[1, 2] * 2 == [1, 2, 1, 2]

## Q:10. What is the difference between the append() and insert() list methods?

append adds it to the back of the list

insert, and the parameters, allows you to put it in a specific spot.

## Q:11. What are two ways to remove values from a list?

remove by the index
and remove by the dictionary name


## Q:12. Name a few ways that list values are similar to string values.

strings, you can call their index to get the letter.

dog = brownie
dog[0] will give you the letter 'b'

## Q:13. What is the difference between lists and tuples?

lists use brackets. []

tuple uses paraenthesis ()

where lists can be modified... tuples are not. They're immutable... or you can't change the size of it. But you can modify/override the variables.

Like, you can't append or remove things in a tuple. 

## Q:14. How do you type the tuple value that has just the integer value 42 in it?

imATuple = (42,)

Failing to add that comma means that it thinks it's a variable.

## Q:15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?

CH04\tupleToList.py

On a list, you use the tuple(x)
On a tuple, you use the list(x)


## Q:16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?

They contain references to the list. 

## Q:17. What is the difference between copy.copy() and copy.deepcopy()?

copy creates a new version of that list

deepcopy creates a new version of that list, and all the lists inside of it. The inner lists.