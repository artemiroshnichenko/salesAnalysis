import mysql.connector
from mysql.connector.errors import Error
import pandas as pd

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
    
    def write2 (self):
        self.connect()
        # creating column list for insertion
        cols = "`,`".join([str(i) for i in self.data.columns.tolist()])
        # Insert DataFrame recrds one by one.
        for i,row in self.data.iterrows():
            
            sql = "INSERT INTO `tilda` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
            
            try:
                self.cursor.execute(sql, tuple(row))
            except mysql.connector.errors.IntegrityError as err:
                if err.errno == 1062: 
                    pass
                    #self.update(self.data_load[index])
                else:
                    print('Something wrong:', err)
            # the connection is not autocommitted by default, so we must commit to save our changes
            self.db.commit()
        pass

    def form_data(self):
        records = data.to_records(index=False)
        self.data_load = list(records)

    def insert(self, index):
        if self.source == 'tilda':
            add_data = ('INSERT INTO tilda(id, phone, name, email, utm_source, utm_medium) VALUES (%s,%s, %s, %s, %s, %s)')
        try:
            self.cursor.execute(add_data, tuple(self.data_load[index]))
        except mysql.connector.errors.IntegrityError as err:
            if err.errno == 1062: 
                print(self.data_load[index])
                #self.update(self.data_load[index])
            else:
                print('Something wrong:', err)
        pass

    def update(self, key):
        if 1:
            __flag = False
            print(key)
            read_data = (
                        'SELECT name, email, utm_source, utm_medium FROM sales.tilda WHERE phone = %s' 
                        )
            self.cursor.execute(read_data, (key[0],))
            for (name, email, utm_source, utm_medium) in self.cursor:
                print(key[0], name, email)
            if name != key[1] and key[1] != 'NaN':
                name = key[1]
                __flag = True
            if email != key[2] and key[2] != 'NaN':
                email = key[2]
                __flag = True
            if utm_source != key[3] and key[3] != 'NaN':
                utm_source = key[3]
                __flag = True
            if utm_medium != key[4] and key[4] != 'NaN':
                utm_medium = key[4]
                __flag = True
            if __flag == True:
                update_data = ('UPDATE sales.tilda SET name = %s, email = %s, utm_source = %s, utm_medium = %s')
                self.cursor.execute(update_data, (name, email, utm_source, utm_medium))
                print('update')



    def write(self):
        self.connect()
        self.form_data()
        for i in range(len(self.data_load)):
            print(self.data_load)
            self.insert(i)
            
        self.db.commit()
        self.cursor.close()
        self.db.close()
          

    def read(self):
        pass

    if __name__ == '__main__':
        
        pass
        