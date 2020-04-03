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
    
    def write(self):
        self.connect()
        self.cursor.execute('SELECT idtilda FROM tilda')
        for i in self.cursor:
            pass
        try:
            b = i[0] + 1
        except UnboundLocalError:
            b=0
        if self.source == 'tilda':
            result = [(1,2),('4353453453','34534534534'),("cpc","cpc")]
            add_data = ('INSERT IGNORE into tilda''(idtilda, phone, utm_medium)''VALUES (%s, %s, %s)')
            data_load = (result)
        try:
            self.cursor.executemany(add_data, data_load)
        except mysql.connector.errors.IntegrityError:
            print('wow')
        self.db.commit()
        self.cursor.close()
        self.db.close()

    def read(self):
        pass
        