import pandas as pd


class JsonToDatarame():

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
            billing = order['billing']
            self.find_id(order['meta_data'])
            self.data = self.data.append({'name': billing['first_name'], 
                            'email': billing['email'], 
                            'phone': billing['phone'], 
                            'ga': self.ga, 
                            'fb': self.fb}, ignore_index=True)
    
    def find_id(self, meta):
        self.ga = None
        self.fb = None
        for parametr in meta:
            if parametr['key'] == '_ga':
                self.ga = parametr['value']
            elif parametr['key'] == '_fbp':
                self.fb = parametr['value']
        return self.ga, self.fb
    
def main():
    pass

if __name__ == '__main__':
    main()

        