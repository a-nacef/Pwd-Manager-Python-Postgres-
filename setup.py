import psycopg2
import json

config = json.loads(open("config.json", "r").read())


def setupdb(dbcurr,conn): 
    queries = ["CREATE TABLE platforms(name varchar(20) PRIMARY KEY);", 
    "CREATE TABLE passwords(id bigint DEFAULT nextval('pwd') PRIMARY KEY, val varchar(90), plt varchar(20) REFERENCES platforms(name) ON DELETE CASCADE);"]
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



if __name__ == '__main__':
    print("Welcome to the password manager setup process.")
    #Connect to an existing db
    try:
        conn = psycopg2.connect(f"dbname={config['dbname']} user={config['user']}")
        cur = conn.cursor()
        print("Connected.")
    except:
        print("Connection failed!")
    #create the necessary tables
    setupdb(cur,conn)
    #Create the pgcrypto extension to encrypt the passwords column
    try:
        cur.execute("CREATE EXTENSION pgcrypto;")
    except:
        print("Encryption module already exists.")
    conn.close()