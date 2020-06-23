import mysql.connector
from mysql.connector.errors import Error
import pandas as pd
from MySQL import connect

class Mysql():
    def __init__(self,source,data):
        self.database = 'sales'
        self.data = data
        self.source = source
        super().__init__()
    
    def _connect(self):
        con = connect.connect()
        self.db = mysql.connector.connect(
            host = con['host'],
            port = con['port'],
            user = con['user'],
            passwd = con['passwd'],
            database = self.database
            )
        self.cursor = self.db.cursor()
    
    def write (self):
        self._connect()
        # creating column list for insertion
        cols = '`,`'.join([str(i) for i in self.data.columns.tolist()])
        # Insert DataFrame recrds one by one.
        print(cols)
        for i,row in self.data.iterrows():
            
            sql = 'INSERT INTO `'+ self.source +'` (`' +cols + '`) VALUES (' + '%s,'*(len(row)-1) + '%s)'
            try:
                self.cursor.execute(sql, tuple(row))
            except mysql.connector.errors.IntegrityError as err:
                if err.errno == 1062: 
                    self.update(self.data.iloc[i])
                else:
                    print('Something wrong:', err)
            # the connection is not autocommitted by default, so we must commit to save our changes
            self.db.commit()
        self.cursor.close()
        self.db.close()
        

    def update(self, key):
        if 1:
            __flag__ = False
            __id__ = int(key['id'])
            read_data = (
                        'SELECT name, phone, email, utm_source, utm_medium FROM ' + self.database + '.' + self.source + ' WHERE id = %s' 
                        )
            self.cursor.execute(read_data, (__id__,))
            for (name, phone, email, utm_source, utm_medium) in self.cursor:
                (name, phone, email, utm_source, utm_medium)
            if name != key['name'] and key['name'] != 'NaN':
                name = key['name']
                __flag__ = True
            if email != key['email'] and key['email'] != 'NaN':
                email = key['email']
                __flag__ = True
            if utm_source != key['utm_source'] and key['utm_source'] != 'NaN':
                utm_source = key['utm_source']
                #print('change utm ', utm_source, key['utm_source'])
                __flag__ = True
            if utm_medium != key['utm_medium'] and key['utm_medium'] != 'NaN':
                utm_medium = key['utm_medium']
                __flag__ = True
            if __flag__ == True:
                update_data = ('UPDATE sales.tilda SET name = %s, email = %s, utm_source = %s, utm_medium = %s WHERE id = %s')
                self.cursor.execute(update_data, (name, email, utm_source, utm_medium,__id__))
                #print('update')
                self.db.commit()
          

    def read(self):
        self._connect()
        __utm_source = []
        __utm_medium = []
        for i in range(len(self.data)):
            _flag_ = True
            read_data = ('SELECT utm_source, utm_medium FROM ' + self.database + '.' + self.source + ' WHERE id = %s' )
            self.cursor.execute(read_data, (str(self.data['id'][i]),))
            for (utm_source, utm_medium) in self.cursor:
                __utm_source.append(utm_source)
                __utm_medium.append(utm_medium)
                _flag_ = False
            if _flag_:
                __utm_source.append('Not info')
                __utm_medium.append('Not info')
        self.data['utm_source'] = __utm_source
        self.data['utm_medium'] = __utm_medium
        self.cursor.close()
        self.db.close()
        
    if __name__ == '__main__':
        print(connect.connect())
        pass
        