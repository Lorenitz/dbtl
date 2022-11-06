import os
import sys
#from show import show
#sys.path.insert(0, '...\...\...\GitHub Projects\dbtl\dbtl\app\subcommand')

#from dbtl.app.subcommand import show
#sys.path.insert(0, '/../dbtl/dbtl/app/subcommand/')
from subcommand import show
    
if len (sys.argv) < 2:
    help = """dbtl allows you to transform data in data warehouses

usage:
  dbtl [sub-command]

sub-commands:
  show    Show the transformation that will take place
  lint    Lint SQL files using SQLFluff
  run     Run all transformations
  test    Test transformations in test environment
    """
    
    print(help)
    sys.exit()
    
    
subcommand = sys.argv[1]        

if subcommand == 'show':
   show.show_details()
else:
    print(f'subcommand {subcommand} not found') 

    