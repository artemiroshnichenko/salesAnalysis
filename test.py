from urllib import parse
import numpy as np
import pandas as pd
import json
import csv
from datetime import datetime


def url_parse(url):
    url = dict(parse.parse_qsl(parse.urlsplit(url).query))
    print(url)

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


FILE_LOCATION = './data/chanel.txt'
data = pd.read_csv(FILE_LOCATION, header=None, sep="\t")
print(data)
i = 0
js = {}
while i < len(data):
    data[0][i] = data[0][i].split(',')
    data[0][i][1] = phone_check(data[0][i][1], 'int')
    print(data[0][i], data[0][i+1])
    js.update({data[0][i][1] : data[0][i+1]})
    i += 3
print(js)