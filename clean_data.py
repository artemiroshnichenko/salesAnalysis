import pandas as pd
import math

#remuve all unnecessary characters
def pohone_check(phone):
    j=0
    phone=str(phone)
    while True:
        try:
            if (phone[j].isdigit()!=True):
                phone=phone[:j] + phone[j+1:]
                j=j-1
        except IndexError:
            break
        j+=1
    if len(phone)>10:
        phone=phone[2:]
    return phone

def check_nan(nan):
    if type(nan) != str:
        if math.isnan(nan) == True:
            return 'NaN'
    else: 
        return nan

class Tilda():
    def __init__(self, data):
        self.data = data
    
    def clean_data (self):
        df = []
        df_name = []
        for i in range(len(self.data)):
            if check_nan(self.data['Phone'][i]) != 'NaN':
                df.append(pohone_check(self.data['Phone'][i]))
            else:
                df.append(pohone_check(self.data['телефон'][i]))
            if check_nan(self.data['Name'][i]) != 'NaN':
                df_name.append(check_nan(self.data['Name'][i]))
            else:
                df_name.append(check_nan(self.data['имя'][i]))
        self.data['Phone'] = df
        self.data['Name'] = df_name
        self.data1 = pd.DataFrame({'Phone':[]})
        self.data1['Phone'] = self.data['Phone']
        self.data1['Name'] = self.data['Name']

    
    


