import mysql.connector

class Mysql():
    def __init__(self):
        super().__init__()
    
    def connect (self):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user = 'python',
            passwd = '1111111111',
            database = 'mydb'
            )
        self.cursor = self.db.cursor()    






