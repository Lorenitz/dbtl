import sys
from subcommand.show import show_details
from subcommand.help import show_help
from subcommand.run import run
from subcommand.test import test
     
if len (sys.argv) < 2:
    show_help()
    sys.exit()
    
    
subcommand = sys.argv[1]        

if subcommand == 'show':
   show_details()
elif subcommand =='help':
   show_help()    
elif subcommand =='run':
   run()  
elif subcommand =='test':
   test()        
else:
    print(f'subcommand {subcommand} not found') 