import yaml
from yaml.loader import SafeLoader

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
        