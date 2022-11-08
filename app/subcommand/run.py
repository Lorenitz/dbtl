import psycopg2
 
def run():
    conn=None
    try:
        conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="123456")
        
        #create a cursor
        cur = conn.cursor()
        
        #execute a statement
        cur.execute('SELECT version()')
        
        db_version = cur.fetchone()
        
        print(db_version)
        
    
        cur.close()
    except Exception as error:
        print('Error when running:')
        print(error)  
    finally:
        if conn is not None:      
            #close the communication with the PostgreSQL
            print('Closing database connection.')
            conn.close()