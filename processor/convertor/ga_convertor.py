from numpy import source
import pandas as pd
from datetime import datetime


class GoogleAnaliticsConvertor():

    def __init__(self, raw, columns) -> None:
        self.json = raw
        self.data = pd.DataFrame()
        self.columns = columns

    def get_data(self):
        if len(self.columns) == \
            len(self.json['reports'][0]['data']['rows'][0]['dimensions']) +\
                len(self.json['reports'][0]['data']['rows'][0]['metrics']):
            for row in self.json['reports'][0]['data']['rows']:
                self.data = self.data.append(self.get_data_from_row(row), ignore_index=True)
        else:
            print('Wrong count columns')
        return self.data

    def get_data_from_row(self, row):
        __data = []
        index_timestamp = self.json['reports'][0]['columnHeader']['dimensions'].index('ga:dateHourMinute')
        for dimension in row['dimensions']:
            if row['dimensions'][index_timestamp] == dimension:
                __data.append(datetime.strptime(dimension, '%Y%m%d%H%M'))
            else:
                __data.append(dimension.encode('UTF-8'))
        for metric in row['metrics']:
            __data.append(int(metric['values'][0].split('.')[0]))
        return pd.Series(__data, index=self.columns)

def main():
    pass

if __name__ == '__main__':
    main()