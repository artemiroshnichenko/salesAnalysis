import mysql.connector
from mysql.connector.errors import Error

class Mysql():
    def __init__(self,source,data):
        self.database = 'sales'
        self.data = data
        self.source = source
        super().__init__()
    
    def connect(self):
        self.db = mysql.connector.connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'python',
            passwd = '1111111111',
            database = self.database
            )
        self.cursor = self.db.cursor()    
        return self.cursor
    
    def form_data(self):
        records = self.data.to_records(index=False)
        self.data_load = list(records)

    def insert(self, index):
        if self.source == 'tilda':
            add_data = ('INSERT INTO tilda(phone, name, email, utm_source, utm_medium) VALUES (%s, %s, %s, %s, %s)')
        try:
            self.cursor.execute(add_data, tuple(self.data_load[index]))
        except mysql.connector.errors.IntegrityError as err:
            if err.errno == 1062:
                pass
        pass

    def write(self):
        self.connect()
        self.form_data()
        for i in range(len(self.data_load)):
            self.insert(i)
        self.db.commit()
        self.cursor.close()
        self.db.close()
          

    def read(self):
        pass

    if __name__ == '__main__':
        
        pass
        