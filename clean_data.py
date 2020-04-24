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
    elif '801' in phone:
        phone = ''
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
    elif '907' in phone:
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
        __phone = list()
        __df_phone = []
        __df_name = []
        __df_email = []
        __df_medium = []
        __df_source = []
        self.data['Date'] = self.data['Дата']
        for i in range(len(self.data)):
            if rem_phone(self.data['Номер звонящего'][i]) == '':
                self.data = self.data.drop([i])
            else:
                __df_phone.append(phone_check(self.data['Номер звонящего'][i],'str'))
                __phone.append(phone_check(self.data['Номер звонящего'][i],'int'))
                __df_email.append('NaN')
                __df_name.append('NaN') 
                __df_source.append(check_nan(self.data['utm_source'][i]))
                __df_medium.append(check_nan(self.data['utm_medium'][i]))
        self.data['phone'] = __phone
        self.data['Name'] = __df_name
        self.data['Email'] = __df_email
        self.data['utm_source'] = __df_source
        self.data['utm_medium'] = __df_medium
        self.data['Phone'] = __df_phone
        self.data = self.data.reset_index(drop=True)
        

    def tilda_form(self):
        __phone = list()
        __df_phone = []
        __df_name = []
        __df_email = []
        __df_medium = []
        __df_source = []
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
        self.data['phone'] = __phone
        self.data['Name'] = __df_name
        self.data['Email'] = __df_email
        self.data['utm_source'] = __df_source
        self.data['utm_medium'] = __df_medium
        self.data['Phone'] = __df_phone
    
    def order_form(self):
        __phone = list()
        __df_phone = []
        __df_name = []
        __df_email = []
        __df_medium = []
        __df_source = []
        self.data['Date'] = self.data['Order Date']
        for i in range(len(self.data)):
            __df_phone.append(phone_check(self.data['Phone (Billing)'][i],'str'))
            __phone.append(phone_check(self.data['Phone (Billing)'][i],'int'))
            __df_email.append(check_nan(self.data['Email (Billing)'][i]))
            __df_name.append(check_nan(self.data['First Name (Billing)'][i]))
            if self.data['Custom Fields'][i].find('utm_Field') != -1:
                __df_source.append(self.data['Custom Fields'][i][self.data['Custom Fields'][i].find('utm_Field'):])
            else:
                __df_source.append('NaN')
            __df_medium.append('NaN')
        self.data['phone'] = __phone
        self.data['Name'] = __df_name
        self.data['Email'] = __df_email
        self.data['utm_source'] = __df_source
        self.data['utm_medium'] = __df_medium
        self.data['Phone'] = __df_phone
        self.data = self.data.reset_index(drop=True)
        
    def popup_form(self, lang):
        __phone = list()
        __df_phone = []
        __df_name = []
        __df_email = []
        __df_medium = []
        __df_source = []
        __date = []
        if lang == 'data/popup_ru.csv':
            col = 'tel-853'
        else:
            col = 'tel-749'
        for i in range(len(self.data)):
            __phone.append(phone_check(self.data[col][i],'int'))
            __df_phone.append(phone_check(self.data[col][i],'str'))
            __df_email.append('NaN')
            __df_source.append(check_nan(self.data['url'][i]))
            __df_medium.append('NaN')
            __df_name.append('NaN')
        self.data['phone'] = __phone
        self.data['Name'] = __df_name
        self.data['Email'] = __df_email
        self.data['utm_source'] = __df_source
        self.data['utm_medium'] = __df_medium
        self.data['Phone'] = __df_phone
        self.data['Date'] = self.data['Дата']

    def client_form(self):
        __phone = list()
        __df_phone = []
        __df_name = []
        __df_email = []
        __df_medium = []
        __df_source = []
        __revenue = []
        __profit = []
        __date = []
        for i in range(len(self.data)):
            try:
                __phone.append(phone_check(self.data[0][i][0][1],'int'))
            except ValueError:
                try:
                    __phone.append(phone_check(self.data[0][i][0][0].split(' ')[-1:],'int'))
                except ValueError:
                    print('err no phone num')
                    __phone.append(i)
            __df_phone.append(phone_check(self.data[0][i][0][1],'str'))
            __df_email.append('NaN')
            __df_source.append('NaN')
            __df_medium.append('NaN')
            __df_name.append(self.data[0][i][0][0])
            __revenue.append(self.data[0][i][1])
            __profit.append(self.data[0][i][2])
            __date.append('NaN')
        self.data['phone'] = __phone
        self.data['Name'] = __df_name
        self.data['Email'] = __df_email
        #self.data['utm_source'] = __df_source
        #self.data['utm_medium'] = __df_medium
        self.data['Phone'] = __df_phone
        self.data['revenue'] = __revenue
        self.data['profit'] = __profit
        self.data['Date'] = __date

    def data_to_load_c(self):
        self.data_load = pd.DataFrame()
        self.data_load['id'] = self.data['phone']
        self.data_load['phone'] = self.data['Phone']
        self.data_load['name'] = self.data['Name']
        self.data_load['email'] = self.data['Email']
        #self.data_load['utm_source'] = self.data['utm_source']
        #self.data_load['utm_medium'] = self.data['utm_medium']
        self.data_load['date'] = self.data['Date']
        self.data_load['revenue'] = self.data['revenue']
        self.data_load['profit'] = self.data['profit']

    def data_to_load(self):
        self.data_load = pd.DataFrame()
        self.data_load['id'] = self.data['phone']
        self.data_load['phone'] = self.data['Phone']
        self.data_load['name'] = self.data['Name']
        self.data_load['email'] = self.data['Email']
        self.data_load['utm_source'] = self.data['utm_source']
        self.data_load['utm_medium'] = self.data['utm_medium']
        self.data_load['date'] = self.data['Date']