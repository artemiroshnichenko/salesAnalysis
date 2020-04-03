import mysql.connector

class Mysql():
    def __init__(self):
        super().__init__()
    
    def connect(self):
        self.db = mysql.connector.connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'python',
            passwd = '1111111111',
            database = 'mydb'
            )
        self.cursor = self.db.cursor()    
        return self.cursor
    
    def write(self, name):
        self.connect()
        if name == 'tilda':
            add_data = ('INSERT INTO tilda''(idtilda, phone, utm)''VALUES (%s, %s, %s)')
            data_load = (55,54645,'wedwed')
        try:
            self.cursor.execute(add_data, data_load)
        except mysql.connector.errors.IntegrityError:
            print('wow')
        self.db.commit()
        self.cursor.close()
        self.db.close()

    def read(self):
        pass
        