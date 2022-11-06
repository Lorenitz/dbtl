import os
import sys
from subcommand.show import show_details
    
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
   show_details()
else:
    print(f'subcommand {subcommand} not found') 

    