import os
import sys

    
if len (sys.argv) < 2:
    print('show help')
    sys.exit()
    
    
subcommand = sys.argv[1]        

if subcommand == 'show':
    print('showshow')
else:
    print(f'subcommand {subcommand} not found') 

    