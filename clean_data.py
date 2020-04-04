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
    while len(phone)>10:
        phone=phone[2:]
    return phone

def check_nan(nan):
    if type(nan) != str:
        if math.isnan(nan) == True:
            return 'NaN'
    else: 
        return nan

def duplicate(data):
    flag = data['Phone'].duplicated()
    for i in range(len(flag)):
        if flag[i] == True:
            data = data.drop([i])
    return data


class Tilda():
    def __init__(self, data):
        self.data = data
    
    def clean_data (self):
        df_phone = []
        df_name = []
        df_email = []
        df_medium = []
        df_source = []
        for i in range(len(self.data)):
            if check_nan(self.data['Phone'][i]) != 'NaN':
                df_phone.append(pohone_check(self.data['Phone'][i]))
            else:
                df_phone.append(pohone_check(self.data['телефон'][i]))
            if check_nan(self.data['Name'][i]) != 'NaN':
                df_name.append(check_nan(self.data['Name'][i]))
            else:
                df_name.append(check_nan(self.data['имя'][i]))
            df_email.append(check_nan(self.data['Email'][i]))
            df_source.append(check_nan(self.data['utm_source'][i]))
            df_medium.append(check_nan(self.data['utm_medium'][i]))
        self.data1 = pd.DataFrame({'Phone':[]})
        self.data1['Name'] = df_name
        self.data1['Email'] = df_email
        self.data1['utm_source'] = df_source
        self.data1['utm_medium'] = df_medium
        self.data1['Phone'] = df_phone


if __name__ == '__main__':
    print('erfefe')
    


