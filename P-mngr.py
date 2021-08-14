import psycopg2
from fernet import Fernet
import os


key = bytes(os.environ["pwdkey"], "utf-8")


