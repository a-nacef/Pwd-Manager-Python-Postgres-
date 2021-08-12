import os
import psycopg2



def setupdb(dbcurr,conn): 
    queries = ["CREATE TABLE platforms(name varchar(20) PRIMARY KEY);", "CREATE TABLE passwords(id INT PRIMARY KEY, val varchar(50), plt varchar(20) REFERENCES platforms(name) ON DELETE CASCADE);"]
    dbcurr.execute("""
        SELECT EXISTS(
            SELECT * FROM pg_tables
            where schemaname = 'public'
        );""")
    if(not dbcurr.fetchone()[0]):    
        try:
            for query in queries:
                dbcurr.execute(query)
            conn.commit()
            print("Tables created.")
        except:
            print("Table creation error!")
            conn.close()
            cur.close()



if __name__ == '__main__':
    print("Welcome to the password manager setup process.")
    #Connect to an existing db
    try:
        conn = psycopg2.connect("dbname=PwdManager user=postgres")
        cur = conn.cursor()
        print("Connected.")
    except:
        print("Connection failed!")

    setupdb(cur,conn)