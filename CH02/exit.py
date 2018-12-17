## This will exit from the program if the input type is exit

import sys

while True:
    print('Type exit to exit')
    response = input()
    
    if response == 'exit':
        sys.exit()
    
    print('You typed ' + response + '.')
