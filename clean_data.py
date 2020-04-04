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
        __df_phone = []
        __df_name = []
        __df_email = []
        __df_medium = []
        __df_source = []
        for i in range(len(self.data)):
            if check_nan(self.data['Phone'][i]) != 'NaN':
                __df_phone.append(pohone_check(self.data['Phone'][i]))
            else:
                __df_phone.append(pohone_check(self.data['телефон'][i]))
            if check_nan(self.data['Name'][i]) != 'NaN':
                __df_name.append(check_nan(self.data['Name'][i]))
            else:
                __df_name.append(check_nan(self.data['имя'][i]))
            __df_email.append(check_nan(self.data['Email'][i]))
            __df_source.append(check_nan(self.data['utm_source'][i]))
            __df_medium.append(check_nan(self.data['utm_medium'][i]))
        self.data1 = pd.DataFrame({'Phone':[]})
        self.data1['Name'] = __df_name
        self.data1['Email'] = __df_email
        self.data1['utm_source'] = __df_source
        self.data1['utm_medium'] = __df_medium
        self.data1['Phone'] = __df_phone

    
    


