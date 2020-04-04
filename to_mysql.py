import mysql.connector

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
        return list(records)


    def write(self):
        self.connect()
        self.cursor.execute('SELECT idtilda FROM tilda')
        for i in self.cursor:
            pass
        if self.source == 'tilda':
            add_data = ('INSERT INTO tilda(phone, name, email, utm_source, utm_medium) VALUES (%s, %s, %s, %s, %s)')
            data_load = self.form_data()
        self.cursor.executemany(add_data, data_load)
        self.db.commit()
        self.cursor.close()
        self.db.close()
          

    def read(self):
        pass
        