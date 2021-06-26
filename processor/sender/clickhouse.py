from clickhouse_driver import Client
from clickhouse_driver import connect
from clickhouse_driver.dbapi import cursor
import pandas as pd


class ClickHouseResolver():

    def __init__(self) -> None:
        pass

    def connect_to_client(self, host='localhost', port=9000, \
            database='default', user='default', password=''):
        self.client = Client(host=host, 
                            port=port, 
                            database=database, 
                            user=user, 
                            password=password,
                            settings={'use_numpy': True})
        try:
            self.client.execute('SHOW DATABASES')
        except:
            print('Database does not exist, create databese %s first' % database)
            self.client = Client(host=host, 
                            port=port, 
                            user=user, 
                            password=password)
            self.create_database(database)
        return self.client

    def connect_by_cursor(self, host):
        self.conn = connect(host)
        self.client = self.conn.cursor()
        return self.client

    def create_database(self, database):
        self.client.execute('CREATE DATABASE %s;' % database)
        print('Database %s created' % database)

    def insert(self, table: str, data):
        self.check_table(table)
        self.client.insert_dataframe('INSERT INTO %s VALUES' % table, data)
        pass

    def check_table(self, table):
        f=[]
        for name in self.client.execute('SHOW TABLES'):
            f.append(name[0])
        if table in f:
            return True
        else:
            print('Table does not exist')
            #self.create_table(table)
            return False

    def create_table(self, table):
        #self.client.execute('CREATE TABLE %s' % table)
        pass

    def custom_sql(self, sql):
        self.client.execute(sql)


def main():
    pass

if __name__ == '__main__':
    main()