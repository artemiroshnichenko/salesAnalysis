import rw
import pandas as pd
import clean_data as cd
import to_mysql
import random

UTM_DICT = {
    'NaN':1,
    'Тех поддержка':1,
    'Для исх звонков':1
}


def tilda():
    data = cd.Tilda(rw.r_csv('data/tilda.csv', ';', 0)) #заносим фид в класс
    data.form()
    #print(data.data_load)
    #a=to_mysql.Mysql('tilda',data.data_load)
    #a.write()
    #print('ok')
    return data.data_load

def calls():
    data = cd.Calls(rw.r_csv('data/call.csv', ',', 0))
    data.form()
    return data.data_load

def order():
    data = cd.Orders(rw.r_csv('data/order.csv', ',', 0))
    data.form()
    return data.data_load

def popup():
    lang = ['data/popup_ua.csv','data/popup_ru.csv']
    v = pd.DataFrame()
    for i in lang:
        data = rw.r_csv(i, ',', 0)
        data.rename(columns={'tel-749': 'phone', 'tel-853': 'phone', 'text-635': 'name', 'Date': 'date'}, inplace=True)
        v = pd.concat([v, data], ignore_index=True)
    data = cd.Popups(v)
    data.form()
    return data.data_load

def client():
    data = rw.r_txt('data/июль.txt', 'zzz', 0)
    data = data.drop([0,1,2,3,4,5]).reset_index(drop=True)
    data = cd.Clients(data)
    data.form()
    return data.data_load

def chanel():
    FILE_LOCATION = './data/chanel.txt'
    data = cd.Chanel(pd.read_csv(FILE_LOCATION, header=None, sep="\t"))
    data.form()
    return data.dict

def find(id, data):
    flag = True
    i = 0
    utm = ['-','-']
    while i < len(data) and flag:
        if id == data['id'][i]:
            try:
                if UTM_DICT[data['utm_source'][i]]:
                    utm = ['-','-']
            except KeyError:
                utm = [data['utm_source'][i], data['utm_medium'][i]]
                flag = False
            except TypeError:
                utm = [data['utm_source'][i]]
                flag = False
        i += 1
    return utm

def check():
    d_tilda = tilda()
    d_calls = calls()
    d_order = order()
    d_popup = popup()
    d_client = client()
    d_chanel = chanel()
    res = pd.DataFrame(columns=['client','price', 'revenue', 'utm'])
    utm: dict
    for i in range(len(d_client)):
        utm = find(d_client['id'][i], d_tilda)
        if utm == ['-','-']:
            utm = find(d_client['id'][i], d_order)
        if utm == ['-','-']:
            utm = find(d_client['id'][i], d_popup)
        if utm == ['-','-']:
            utm = find(d_client['id'][i], d_calls)
        if utm == ['-','-']:
            try:
                if d_chanel[d_client['id'][i]] == 'google':
                    utm = [d_chanel[d_client['id'][i]],  random.choices(['ads', 'organic'], weights=[70, 30])[0]]
                else:
                    utm = [d_chanel[d_client['id'][i]], '-']
            except KeyError:
                pass
        res = res.append({'client':d_client['client'][i], 'price':d_client['price'][i], 'revenue':d_client['revenue'][i], 'utm':utm}, ignore_index=True)
    return res


def main():
    res = check()
    print(res)
    rw.w_csv('./data/res.csv', res)
    #check()
    #order()
    #print(popup())
    #calls()
    #tilda()
    #data = client()
    #sql = to_mysql.Mysql('lead', data)
    #sql.read()
    #print(sql.data)
    #rw.w_csv('data/res.csv',sql.data)
    #tilda()
    #c = client()
    #res = check(c, t)
    #rw.w_csv('data/res.csv',res)
    #order()
    #print(client())
    #chanel()
    print('ok')


if __name__ == '__main__':
    import timeit
    load = 'main'
    print(timeit.timeit(load+'()', setup="from __main__ import " + load,number=1))
