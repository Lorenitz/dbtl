import psycopg2
import yaml
import os
from yaml.loader import SafeLoader


dir_path_models=r'models/'
dir_path_tests=r'tests/' 
 
def test():
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
        count_models =0
        count_tests=0
        # Iterate directory
        for path in os.listdir(dir_path_models):
            # check if current path is a file
            if os.path.isfile(os.path.join(dir_path_models, path)):
                count_models += 1
       
        for path in os.listdir(dir_path_tests):
            # check if current path is a file
            if os.path.isfile(os.path.join(dir_path_tests, path)):
                count_tests += 1
                
        print(f"Found {count_models} models, {count_tests} test \n")
        print("| Concurrency: 1 thread (target='prod') \n")
        
        
        iter_file=0
        error_file=0
        error_messages=[]
        dots=".............................."
        # For each model in /models 
        for path in os.listdir(dir_path_tests):
            file_name = os.path.join(dir_path_tests, path)
            if os.path.isfile(file_name):
                iter_file+=1    
                print(f"| {iter_file} of {count_tests} START {file_name}{dots[len(file_name):]}[RUN]" )
                try:
                    with open(file_name) as f:
                        
                        lines = f.readlines()

                        statement = ''.join(lines)
                        
                        #create a cursor
                        cur = conn.cursor()
                        
                        #execute a statement
                        cur.execute(statement)
                        results=cur.fetchall()
                        
                        if len(results):
                            #Raise Exception that will be caught by the try block
                            raise Exception(str(results))
                        cur.close()
                    print(f"| {iter_file} of {count_tests} OK {file_name}...{dots[len(file_name):]}[PASS in 1.00s]")
                except Exception as error:
                   print(f"| {iter_file} of {count_tests} ERROR {file_name}...{dots[len(file_name):]}[ERROR in 1.00s]")
                   error_messages.append(error)
                   
        print('| Finished running ' +str(count_tests)+ ' models in 3.00s. \n')  
        
        pass_without_errors=count_tests-len(error_messages)
        
        if len(error_messages)==0:
            print('Completed successfully\n')
            print('DONE. PASS='+str(count_tests)+ ' ERROR=0 TOTAL='+str(count_tests))
        else:
           print(f"Completed with {len(error_messages)} errors. \n")
           
           #For each error found in models:
           for error_message in error_messages:
                print(f"Error in {file_name}. \nAffected rows:")
                print(error_message)
           print(f"DONE. PASS={pass_without_errors} ERROR={len(error_messages)} TOTAL={count_tests}")          
        
    except Exception as error:
        print('Error when running:')
       
    finally:
        if conn is not None:      
            #close the communication with the PostgreSQL
            print('Closing database connection.')
            conn.commit()
            conn.close()