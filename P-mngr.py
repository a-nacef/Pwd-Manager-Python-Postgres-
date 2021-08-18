import psycopg2
from fernet import Fernet
import os
import json
import re

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
    pwd = encryptdata(input("Enter a password\n"))
    platform = input("Enter a platform\n")
    curr.execute(f"SELECT EXISTS( SELECT name FROM platforms where name = '{platform}')")
    if curr.fetchone()[0]:
        #used replace here cause using str() on a bytes string keep the leading 'b' for some reason?
        curr.execute(f"INSERT INTO passwords (val,plt) VALUES ({str(pwd).replace('b', '', 1)}, '{platform}');")
    else:
        print("Platform doesnt exist.")

def addplatform():
    platform = input("Enter a platform\n")
    curr.execute(f"INSERT INTO platforms (name) VALUES ('{platform}');")
    return



def getpassword():
    platform = input("Enter a platform\n")
    curr.execute(f"SELECT val FROM passwords where plt = '{platform}'")
    data = curr.fetchall()
    for pwd in data:
        yield bytes(pwd[0], "utf-8")
        



def main():
    command = ''
    print("Welcome to your password manager!")
    while(command.lower() != 'q'):
        command = input("""
           a: Add a password\n
           b: Add a platform\n
           c: Get password\n
           q: quit\n
        """)
        if command.lower() == 'a':
            addpassword()
        elif command.lower() == 'b':
            addplatform()
        elif command.lower() == 'c':
            passwords = getpassword()
            for pwd in passwords:
                temp = str(decryptdata(pwd))
                print(temp[2:len(temp)-1])
    conn.commit()
    conn.close()
                 
if __name__ == '__main__':
    main()