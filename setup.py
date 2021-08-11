import os
import psycopg2



def setupdb(dbcurr,conn):
    
    dbcurr.execute("""
        SELECT EXISTS(
            SELECT * FROM pg_tables
            where schemaname = 'public'
        );""")
    if(not dbcurr.fetchone()[0]):    
        try:    
            dbcurr.execute("CREATE TABLE platforms(name varchar(20) PRIMARY KEY);")
            conn.commit()
            dbcurr.execute("CREATE TABLE passwords(id INT PRIMARY KEY, val varchar(50), plt varchar(20) REFERENCES platforms(name) ON DELETE CASCADE);")
            conn.commit()
            print("Tables created.")
        except:
            print("Table creation error!")
            conn.close()
            cur.close()


print("Welcome to the password manager setup process.")
#Connect to an existing db
try:
    conn = psycopg2.connect("dbname=PwdManager user=postgres")
    cur = conn.cursor()
    print("Connected.")
except:
    print("Connection failed!")

setupdb(cur,conn)

passphrase = input("Please enter a passphrase, this will be used to enter the manager and will determine how data is encrypted.\n")
os.environ.update({"Pmngr_pwd":passphrase})

#print("Testing env write:\n")
#print(os.getenv("Pmngr_pwd"))
conn.close()
cur.close()