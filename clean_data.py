import pandas as pd
import math

#remuve all unnecessary characters
def pohone_check(phone):
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
    return int(phone)

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

    def form_chart(self):
        self.data = self.data.drop(columns=['Delivery','payment','comment_form','адрес_доставки','оплата',
                                'Textarea','question','Podval','requisites','uniqa','Адреса_доставки','имя','телефон','доставка',
                                'Телефон_для_акции_бесплатной_установки','city','mymetroinput','job','brand','Статус оплаты',
                                'Способ оплаты','Сумма заказа','tranid','formid','formname','paymentsystem','Способ_доставки',
                                'Вы_живете_в','step2','step3','Сколько_комнат_или_помещений_требует_защиты','Tag','Status ID','web-stie'])
        pass

    def form_phone_nuber(self):
        phone = list()
        for i in range(len(self.data)):
            if check_nan(self.data['Phone'][i]) == 'NaN':
                self.data['Phone'][i] = self.data['телефон'][i]
                self.data['Name'][i] = self.data['телефон'][i]
            phone.append(pohone_check(self.data['Phone'][i]))
        self.data['phone'] = phone
    
    


