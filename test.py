#settings.py
import os
from os.path import join, dirname
from dotenv import load_dotenv
 
dotenv_path = './Configuration/config.env'
load_dotenv(dotenv_path)
 
# Accessing variables.
status = os.getenv('HOST_NAME')
secret_key = os.getenv('H_PORT')
 
# Using variables.
print(status)
print(secret_key)