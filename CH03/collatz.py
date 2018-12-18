
def collatz(number):
    if number % 2 == 0:
        return(number // 2)
    else:
        return(3 * number + 1)



print("Pick a number")
try: 
    guess = int(input())
except ValueError:
    print("Enter a number bro!")


while guess != 1:     
    print(guess)
    guess = collatz(guess)

print(guess)
print("You did it!")
