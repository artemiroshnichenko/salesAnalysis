import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup
import re

class BinotelConvertor():

    def __init__(self, raw):
        self.raw = raw
        self.data = pd.DataFrame()

    def incoming(self):
        raw = self.raw['callDetails']
        for call_id in raw:
            try:
                source = raw[call_id]['pbxNumberData']['name'].encode('UTF-8')
            except KeyError as error:
                if error == 'name':
                    source = ''
                else:
                    print('KeyError ', error)
            try:
                manager = raw[call_id]['employeeData']['name'].encode('UTF-8')
            except TypeError:
                manager = ''
            self.data = self.data.append({'id': call_id, 
                                        'phone': raw[call_id]['externalNumber'], 
                                        'source': source, 
                                        'manager': manager, 
                                        'billsec': raw[call_id]['billsec'],
                                        'timestamp': datetime.fromtimestamp(int(raw[call_id]['startTime']))}, 
                                        ignore_index=True)
        return self.data.astype({'billsec': int})
    
    def call_tracking(self):
        raw = self.raw['callDetails']
        for call_id in raw:
            try:
                manager = raw[call_id]['employeeData']['name'].encode('UTF-8')
            except TypeError:
                    manager = ''
            self.data = self.data.append({'id': call_id, 
                                'phone': raw[call_id]['externalNumber'], 
                                'ga_id': raw[call_id]['callTrackingData']['gaClientId'], 
                                'manager': manager, 
                                'billsec': raw[call_id]['billsec'],
                                'timestamp': datetime.fromtimestamp(int(raw[call_id]['startTime']))},
                                 ignore_index=True)
        return self.data.astype({'billsec': int})

    def get_call(self):
        soup = BeautifulSoup(self.raw, 'html.parser')
        data = pd.DataFrame()
        leng = len(soup.find_all('a', class_='number', href=True))
        for i in range(leng):
            data = data.append({'phone': soup.find_all('a', class_='number', href=True)[i].text,
                'billsec': self.to_sec(soup.find_all('div', class_='right-cell billsec')[i].text),
                'manager': self.check_manager(soup.find_all('td', 
                        class_='to-whom-calling')[i].find('a', class_='name')),
                'timestamp': datetime.strptime(soup.find_all('td', class_='call-time')
                        [i].text.replace(u'\xa0', u''), '%H:%M    %d.%m.%Y'),
                'ga_id': soup.find_all('div', class_='gc-detail-overlay requestMask22333')[i].find('a',
                        text=re.compile(r'\d{6,9}\.\d{10}')).text}, ignore_index=True)
        return data

    def to_sec(self, sec):
        if sec == '-':
            return 0
        else:
            return (datetime.strptime(sec, '%M:%S') - datetime(1900,1,1)).total_seconds()

    def check_manager(self, manager):
        try:
            return manager.text
        except AttributeError:
            return ''


def main():
    pass

if __name__ == '__main__':
    main()
