import psycopg2
import yaml
import os
from yaml.loader import SafeLoader


dir_path=r'models/'
 
def run():
    conn=None
    
    with open('.dbt/profiles.yml') as f:
        data = yaml.load(f, Loader=SafeLoader)
    try:
        conn = psycopg2.connect(
        host= data['prod']['host'],
        database=data['prod']['dbname'],
        user=data['prod']['user'],
        password=data['prod']['password']
        )
        
        # For each model in /models {
        for path in os.listdir(dir_path):
            file_name = os.path.join(dir_path, path)
            if os.path.isfile(file_name):
                with open(file_name) as f:
                    lines = f.readlines()

                    statement = ''.join(lines)
                    
                    #create a cursor
                    cur = conn.cursor()
                    
                    #execute a statement
                    cur.execute(statement)
                    
                    #db_version = cur.fetchone()
                    
                    #print(db_version)
                    
                
                    cur.close() 
    except Exception as error:
        print('Error when running:')
        print(error)  
    finally:
        if conn is not None:      
            #close the communication with the PostgreSQL
            print('Closing database connection.')
            conn.commit()
            conn.close()