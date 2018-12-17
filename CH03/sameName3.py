def spam():
    global eggs
    eggs = 'spam' #thisis the global

def bacon():
    eggs = 'bacon' #this is the local

def ham(): 
    print(eggs) # this is the global

eggs = 42 # this is the global

spam()

print(eggs)