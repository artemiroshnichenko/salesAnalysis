import pandas as pd

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


class Tilda():
    def __init__(self, data):
        self.data = data
    
    def clean_data (self):
        for i in range(len(self.data)):
             df = pohone_check(self.data['Phone'][i])
        self.data['Phone'] = df
    


