import psycopg2
from fernet import Fernet
import os
import json


config = json.loads(open("config.json", "r").read())
command = ""
key = bytes(os.environ["pwdkey"], "utf-8")
f = Fernet(key)
conn = psycopg2.connect(f"dbname={config['dbname']} user={config['user']}")
curr = conn.cursor()

def encryptdata(msg):
    return f.encrypt(msg)

def decryptdata(msg):
    return f.decrypt(msg)


def addpassword():
    pwd = encryptdata(input("Enter a password\n")).decode("utf-8")
    platform = input("Enter a platform\n")
    curr.execute(f"SELECT EXISTS( SELECT name FROM platforms where name = '{platform}')")
    if curr.fetchone()[0]:
        curr.execute(f"INSERT INTO passwords (val,plt) VALUES ('{pwd}', '{platform}');")
    else:
        print("Platform doesnt exist.")

def addplatform():
    platform = input("Enter a platform\n")
    curr.execute(f"INSERT INTO platforms (name) VALUES ('{platform}');")
    return



def getpassword():
    platform = input("Enter a platform\n")
    return decryptdata(curr.execute(f"SELECT val FROM passwords where plt = {platform}").fetchall())





def main():
    command = ''
    while(command.lower() != 'q'):
        command = input("""Welcome to your password manager, press Q to quit the program\n
           a: Add a password\n
           b: Add a platform\n
           c: Get password\n
        """)
        if command.lower() == 'a':
            addpassword()
        elif command.lower() == 'b':
            addplatform()
        elif command.lower() == 'c':
            passwords = getpassword()
            for pwd in passwords:
                print(pwd)
    conn.commit()
    conn.close()
                 
if __name__ == '__main__':
    main()