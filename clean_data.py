import pandas as pd
import math
import re
from urllib import parse


#remuve all unnecessary characters
def phone_check(phone, typ):
    j=0
    phone=str(phone)
    if phone == 'nan':
        return 0
    elif phone == '':
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
        if phone == '':
            return 0
        else:
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

def parse(mark, url):
    result = re.search(r'utm_{}=(.+?)(&|$)'.format(mark), url)
    if result:
        return result.group(1)
    return None

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

def url_parse(url):
    return dict(parse.parse_qsl(parse.urlsplit(url).query))

class Data:
    def __init__(self, data):
        self.data = data

class Tilda(Data):
    def form(self):
        self.data_load = pd.DataFrame()
        __phone = []
        __df_phone = []
        __df_name = []
        __df_email = []
        __df_medium = []
        __df_source = []
        for i in range(len(self.data)):
            if check_nan(self.data['phone'][i]) != 'NaN':
                __df_phone.append(phone_check(self.data['phone'][i],'str'))
            else:
                __df_phone.append(phone_check(self.data['телефон'][i],'str'))
            if check_nan(self.data['name'][i]) != 'NaN':
                __df_name.append(check_nan(self.data['name'][i]))
            else:
                __df_name.append(check_nan(self.data['имя'][i]))
            __df_email.append(check_nan(self.data['email'][i]))
            __url = url_parse(self.data['referer'])
            try:
                __df_source.append(__url['utm_source'])
            except KeyError:
                __df_source.append('google')
            try:
                __df_source.append(__url['utm_medium'])
            except KeyError:
                __df_source.append('ads')
            __phone.append(int(__df_phone[i]))
        self.data_load['id'] = __phone
        self.data_load['name'] = __df_name
        self.data_load['email'] = __df_email
        self.data_load['utm_source'] = __df_source
        self.data_load['utm_medium'] = __df_medium
        self.data_load['phone'] = __df_phone
        self.data_load['date'] = self.data['created']
    
class Calls(Data):
    def form(self):
        self.data_load = pd.DataFrame()
        __phone = []
        __df_phone = []
        __df_name = []
        __df_email = []
        __df_medium = []
        __df_source = []
        self.data_load['date'] = self.data['Дата']
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
        self.data_load['id'] = __phone
        self.data_load['name'] = __df_name
        self.data_load['email'] = __df_email
        self.data_load['utm_source'] = __df_source
        self.data_load['utm_medium'] = __df_medium
        self.data_load['phone'] = __df_phone

class Orders(Data):
    def form(self):
        self.data_load = pd.DataFrame()
        __phone = []
        __df_phone = []
        __df_name = []
        __df_email = []
        __df_medium = []
        __df_source = []
        self.data_load['date'] = self.data['Order Date']
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
        self.data_load['id'] = __phone
        self.data_load['name'] = __df_name
        self.data_load['email'] = __df_email
        self.data_load['utm_source'] = __df_source
        self.data_load['utm_medium'] = __df_medium
        self.data_load['phone'] = __df_phone

class Popups(Data):
    def form(self):
        self.data_load = pd.DataFrame()
        __phone = []
        __df_phone = []
        __df_name = []
        __df_email = []
        __df_medium = []
        __df_source = []
        __date = []
        for i in range(len(self.data)):
            __phone.append(phone_check(self.data['phone'][i],'int'))
            __df_phone.append(phone_check(self.data['phone'][i],'str'))
            __df_email.append('NaN')
            __df_source.append(check_nan(self.data['parameter-string-field'][i]))
            __df_medium.append('NaN')
            __df_name.append('NaN')
        self.data_load['id'] = __phone
        self.data_load['name'] = __df_name
        self.data_load['email'] = __df_email
        self.data_load['utm_source'] = __df_source
        self.data_load['utm_medium'] = __df_medium
        self.data_load['phone'] = __df_phone
        self.data_load['date'] = self.data['date']

class Clients(Data):
    def form(self):
        self.data_load = pd.DataFrame()
        __id = []
        __client = []
        __phone = []
        __price = []
        __revenue = []
        for i in range(len(self.data)-1):
            var = self.data[0][i].split('\t')
            name = var[0].split(',')[0]
            try:
                num = var[0].split(',')[1]
            except IndexError:
                num = name.split(' ')[-1]
            if num == '':
                num = name.split(' ')[-1]
            __client.append(name)
            __id.append(phone_check(num,'int'))
            __phone.append(phone_check(num,'str'))
            try:
                __price.append(var[1].replace('\xa0','').replace(',','.'))
            except IndexError:
                __price.append(0)
            try:
                __revenue.append(var[2].replace('\xa0','').replace(',','.'))
            except IndexError:
                __revenue.append(0)
        self.data_load['id'] = __id
        self.data_load['client'] = __client
        self.data_load['phone'] = __phone
        self.data_load['price'] = __price
        self.data_load['revenue'] = __revenue
  

