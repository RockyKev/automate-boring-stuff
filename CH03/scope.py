def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()

# to pass the local value over
# def spam():
#     eggs = 99
#     eggs = bacon()
#     print(eggs)

# def bacon():
#     ham = 101
#     eggs = 0
#     return eggs

# spam()