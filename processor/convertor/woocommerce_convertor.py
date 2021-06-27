import pandas as pd
from datetime import datetime


class WoocommerceConvertor():

    def __init__(self, raw):
        self.json = raw
        self.data = pd.DataFrame()

    def get_data_frame(self):
        """Convert JSON to DataFrame
        Args: 
            json
        Return: 
            DataFrame"""
        
        for page in self.json:
            self.page_convertor(page)
        return self.data.drop_duplicates().reset_index().drop(columns='index')

    def page_convertor(self, page):
        for order in page:
            time = datetime.strptime(order['date_created'], '%Y-%m-%dT%H:%M:%S')
            billing = order['billing']
            self.find_id(order['meta_data'])
            self.data = self.data.append({'name': billing['first_name'], 
                            'email': billing['email'], 
                            'phone': self.formate_phone(billing['phone']), 
                            'ga_id': self.ga, 
                            'fb_id': self.fb,
                            'timestamp': time}, ignore_index=True)
    
    def find_id(self, meta):
        self.ga = ''
        self.fb = ''
        for parametr in meta:
            if parametr['key'] == '_ga':
                self.ga = parametr['value'][6:]
            elif parametr['key'] == '_fbp':
                self.fb = parametr['value'][5:]
        return self.ga, self.fb

    def formate_phone(self, phone):
        phone = str(phone)
        num = ''
        for element in phone:
            if element.isdigit() == True:
                num += element
        if len(num) > 10:
            num = num[len(num)-10:]
        return num
    
def main():
    pass

if __name__ == '__main__':
    main()

        