## Purposely erroneous code
## to show that locals cannot touch globals

def spam():
    print(eggs) # ERROR!
    eggs = 'spam local'

eggs = 'global'

spam()
