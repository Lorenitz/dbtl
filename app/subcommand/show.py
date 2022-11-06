import yaml
import os
from yaml.loader import SafeLoader

dir_path=r'models/'
# list to store files
res = []

def show_details():
    with open('.dbt/profiles.yml') as f:
        data = yaml.load(f, Loader=SafeLoader)
        print('prod warehouse:')
        print(f"  {data['prod']['type']}: {data['prod']['host']}")
        print(f"  dbname: {data['prod']['dbname']}\n")
        print('test warehouse:')
        print(f"  {data['test']['type']}: {data['test']['host']}")
        print(f"  dbname: {data['test']['dbname']}\n")
        
        print('sql files:')
        
    for path in os.listdir(dir_path):
        file_name = os.path.join(dir_path, path)
        
        # check if current path is a file
        if os.path.isfile(file_name):
           # res.append(file_name)
            print(f"  {file_name}")
       