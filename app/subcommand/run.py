import psycopg2
import yaml
import os
from yaml.loader import SafeLoader


dir_path=r'models/'
 
def run():
    conn=None
    count=0
    with open('.dbt/profiles.yml') as f:
        data = yaml.load(f, Loader=SafeLoader)
    try:
        conn = psycopg2.connect(
        host= data['prod']['host'],
        database=data['prod']['dbname'],
        user=data['prod']['user'],
        password=data['prod']['password']
        )
        
        print("Running with dbtl")
        
        # Counting the number of files in folder
        count = 0
        # Iterate directory
        for path in os.listdir(dir_path):
            # check if current path is a file
            if os.path.isfile(os.path.join(dir_path, path)):
                count += 1
       
        print(f"Found {count} models, 0 test \n")
        print("| Concurrency: 1 thread (target='prod') \n")
        
        
        iter_file=0
        error_file=0
        dots=".............................."
        # For each model in /models {
        for path in os.listdir(dir_path):
            file_name = os.path.join(dir_path, path)
            if os.path.isfile(file_name):
                iter_file+=1    
                print(f"| {iter_file} of {count} START {file_name}{dots[len(file_name):]}[RUN]" )
                try:
                    with open(file_name) as f:
                        
                        lines = f.readlines()

                        statement = ''.join(lines)
                        
                        #create a cursor
                        cur = conn.cursor()
                        
                        #execute a statement
                        cur.execute(statement)
                    
                        cur.close()
                    print(f"| {iter_file} of {count} OK {file_name}...{dots[len(file_name):]}[SUCCESS in 1.00s]")
                except Exception as error:
                   error_file+=1
                   print(f"| {iter_file} of {count} ERROR {file_name}...{dots[len(file_name):]}[ERROR in 1.00s]")
                   error_message=error

        print('| Finished running ' +str(count)+ ' models in 3.00s. \n')  
        pass_without_errors=count-error_file
        if error_file==0:
            print('Completed successfully\n')
            print('DONE. PASS='+str(count)+ ' ERROR=0 TOTAL='+str(count))
        else:
           print(f"Completed with {error_file} errors. \n")
           
           print(f"Error in {file_name}")
           print(error_message)
           print('DONE. PASS='+str(pass_without_errors)+ ' ERROR='+str(error_file)+ ' TOTAL='+str(count))
           
        
    except Exception as error:
        print('Error when running:')
       
    finally:
        if conn is not None:      
            #close the communication with the PostgreSQL
            print('Closing database connection.')
            conn.commit()
            conn.close()