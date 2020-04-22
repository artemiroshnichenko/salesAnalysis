import pandas as pd
import math

#remuve all unnecessary characters
def pohone_check(phone, typ):
    j=0
    phone=str(phone)
    if phone == 'nan':
        return 0
    while True:
        try:
            if (phone[j].isdigit()!=True):
                phone=phone[:j] + phone[j+1:]
                j=j-1
        except IndexError:
            break
        j+=1
    while len(phone)>10:
        phone=phone[2:]
    if typ == 'int':
        return int(phone)
    elif typ == 'str':
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
        prev = 1
        j = 0
        for i in range(len(self.data)):
            if self.data['phone'][i] == prev:
                j += 1
                if type(self.data['utm_source'][i-j]) != str:
                    if type(self.data['utm_source'][i]) == str: 
                        self.data['utm_source'][i-j] = self.data['utm_source'][i]
                        self.data['utm_medium'][i-j] = self.data['utm_medium'][i]
                self.data = self.data.drop([i])
            else:
                prev = self.data['phone'][i]
                j = 0
        self.data = self.data.reset_index(drop=True)
        self.data_to_load()

    def form_phone_nuber(self):
        __phone = list()
        __df_phone = []
        __df_name = []
        __df_email = []
        __df_medium = []
        __df_source = []
        for i in range(len(self.data)):
            if check_nan(self.data['Phone'][i]) != 'NaN':
                __df_phone.append(pohone_check(self.data['Phone'][i],'str'))
            else:
                __df_phone.append(pohone_check(self.data['телефон'][i],'str'))
            if check_nan(self.data['Name'][i]) != 'NaN':
                __df_name.append(check_nan(self.data['Name'][i]))
            else:
                __df_name.append(check_nan(self.data['имя'][i]))
            __df_email.append(check_nan(self.data['Email'][i]))
            __df_source.append(check_nan(self.data['utm_source'][i]))
            __df_medium.append(check_nan(self.data['utm_medium'][i]))
            __phone.append(pohone_check(self.data['Phone'][i],'int'))
        self.data['phone'] = __phone
        self.data['Name'] = __df_name
        self.data['Email'] = __df_email
        self.data['utm_source'] = __df_source
        self.data['utm_medium'] = __df_medium
        self.data['Phone'] = __df_phone
    

    def data_to_load(self):
        self.data_load = pd.DataFrame()
        self.data_load['id'] = self.data['phone']
        self.data_load['phone'] = self.data['Phone']
        self.data_load['name'] = self.data['Name']
        self.data_load['email'] = self.data['Email']
        self.data_load['utm_source'] = self.data['utm_source']
        self.data_load['utm_medium'] = self.data['utm_medium']