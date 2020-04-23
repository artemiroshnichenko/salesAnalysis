import pandas as pd
import math

#remuve all unnecessary characters
def phone_check(phone, typ):
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

def rem_phone(phone):
    phone=phone_check(phone,'str')
    phone=str(phone)
    if phone=='':
        pass
    elif  'номер скрыт оператором' in phone.lower():
        phone =''
    elif '901' in phone:
        phone = ''
    elif '902' in phone:
        phone = ''
    elif '903' in phone:
        phone = ''
    elif '904' in phone:
        phone = ''
    elif '905' in phone:
        phone = ''
    elif '906' in phone:
        phone = ''   
    elif '0442994990' in phone:
        phone = '' 
    elif '0800210592' in phone:
        phone = '' 
    elif '0800218616' in phone:
        phone = ''  
    elif '0800218626' in phone:
        phone = ''  
    elif '0800218635' in phone:
        phone = '' 
    elif '0800218636' in phone:
        phone = '' 
    elif '0800218323' in phone:
        phone = '' 
    elif '0800218345' in phone:
        phone = '' 
    elif '0442994700' in phone:
        phone = '' 
    elif '0800211317' in phone:
        phone = '' 
    elif '0800211407' in phone:
        phone = ''  
    elif '0800212060' in phone:
        phone = '' 
    elif '0800212067' in phone:
        phone = '' 
    elif '0800212372' in phone:
        phone = ''  
    elif '0800212377' in phone:
        phone = ''  
    elif '0931706821' in phone:
        phone = ''  
    elif '0931706437' in phone:
        phone = ''  
    elif '0800201723' in phone:
        phone = ''
    elif '0800201843' in phone:
        phone = ''
    elif '4958775599' in phone:
        phone = ''
    return phone

class Data():
    def __init__(self, data):
        self.data = data
    
    def  remove_duplicates(self):
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

    def calls_form(self):
        for i in range(len(self.data)):
            if rem_phone(self.data['Номер звонящего'][i]) == '':
                self.data.drop([i])
            else:
                self.data['Phone'][i] = phone_check(self.data['Номер звонящего'][i],'str')
                self.data['phone'][i] = phone_check(self.data['Номер звонящего'][i],'int')
                self.data['Email'][i] = 'NaN'
                self.data['Name'][i] = 'NaN'
                self.data['utm_source'][i] = check_nan(self.data['utm_source'][i])
                self.data['utm_medium'][i] = check_nan(self.data['utm_medium'][i])
        pass

    def form_phone_nuber(self):
        __phone = list()
        __df_phone = []
        __df_name = []
        __df_email = []
        __df_medium = []
        __df_source = []
        __date = []
        for i in range(len(self.data)):
            if check_nan(self.data['Phone'][i]) != 'NaN':
                __df_phone.append(phone_check(self.data['Phone'][i],'str'))
            else:
                __df_phone.append(phone_check(self.data['телефон'][i],'str'))
            if check_nan(self.data['Name'][i]) != 'NaN':
                __df_name.append(check_nan(self.data['Name'][i]))
            else:
                __df_name.append(check_nan(self.data['имя'][i]))
            __df_email.append(check_nan(self.data['Email'][i]))
            __df_source.append(check_nan(self.data['utm_source'][i]))
            __df_medium.append(check_nan(self.data['utm_medium'][i]))
            __phone.append(phone_check(self.data['Phone'][i],'int'))
            __date.append(check_nan(self.data['Date'][i]))
        self.data['phone'] = __phone
        self.data['Name'] = __df_name
        self.data['Email'] = __df_email
        self.data['utm_source'] = __df_source
        self.data['utm_medium'] = __df_medium
        self.data['Phone'] = __df_phone
        self.data['Date'] = __date
    

    def data_to_load(self):
        self.data_load = pd.DataFrame()
        self.data_load['id'] = self.data['phone']
        self.data_load['phone'] = self.data['Phone']
        self.data_load['name'] = self.data['Name']
        self.data_load['email'] = self.data['Email']
        self.data_load['utm_source'] = self.data['utm_source']
        self.data_load['utm_medium'] = self.data['utm_medium']
        self.data_load['date'] = self.data['Date']