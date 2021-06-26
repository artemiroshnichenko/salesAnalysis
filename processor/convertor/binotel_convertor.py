import pandas as pd


class BinotelConvertor():

    def __init__(self, raw):
        self.json = raw
        self.data = pd.DataFrame()

    def incoming(self):
        raw = self.json['callDetails']
        for call_id in raw:
            try:
                source = raw[call_id]['pbxNumberData']['name'].encode('UTF-8')
            except KeyError as error:
                if error == 'name':
                    source = None
                else:
                    print('KeyError ', error)
            try:
                manager = raw[call_id]['employeeData']['name'].encode('UTF-8')
            except TypeError:
                    manager = None
            self.data = self.data.append({'id': call_id, 'phone': raw[call_id]['externalNumber'], 'source': source, 
                                'manager': manager, 'billsec': int(raw[call_id]['billsec'])}, ignore_index=True)
        return self.data
    
    def call_tracking(self):
        raw = self.json['callDetails']
        for call_id in raw:
            try:
                manager = raw[call_id]['employeeData']['name'].encode('UTF-8')
            except TypeError:
                    manager = None
            self.data = self.data.append({'id': call_id, 
                                'phone': raw[call_id]['externalNumber'], 
                                'ga': raw[call_id]['callTrackingData']['gaClientId'], 
                                'manager': manager, 
                                'billsec': raw[call_id]['billsec']}, ignore_index=True)
        return self.data


def main():
    pass

if __name__ == '__main__':
    main()
