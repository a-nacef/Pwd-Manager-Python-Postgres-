#import psycopg2
from fernet import Fernet
import os
import keyboard
import uuid

command = ""
key = bytes(os.environ["pwdkey"], "utf-8")
f = Fernet(key)
conn = psycopg2.connect(f"dbname={config['dbname']} user={config['user']}")
curr = conn.cursor()

def encryptdata(msg):
    return f.encrypt(msg)

def decryptdata(msg):
    return f.decrypt(msg)


def addpassword(pwd, platform):
    return curr.execute("")



def addplatform(platform):
    return


def getpassword(platform):
    return





def main():
    print("Welcome to your password manager, press Q to quit the program")
    while(lower(command) != 'q'):
        print(""""
           a: Add a password
           b: Add a platform
           c: Get password
        """)
        if lower(command) = 'a':
            addpassword()
        elif lower(command) = 'b':
            addplatform()
        elif lower(command) = 'c':
            getpassword()
    conn.commit()
    conn.close()
                 
if __name__ == '__main__':
    main()