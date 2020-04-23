import rw
import pandas as pd
import clean_data as cd
import to_mysql

def tilda():
    data = cd.Data(rw.r_csv('data/tilda.csv', ';', 0))
    data.tilda_form()
    data.data = data.data.sort_values(by=['phone']).reset_index(drop=True)
    data.remove_duplicates()
    #print(data.data)
    #print(tilda.data_load)
    a=to_mysql.Mysql('tilda',data.data_load)
    a.write()
    print('ok')

def calls():
    data = cd.Data(rw.r_csv('data/call.csv', ',', 0))
    data.calls_form()
    data.data = data.data.sort_values(by=['phone']).reset_index(drop=True)
    data.remove_duplicates()
    data.data_to_load()
    print(data.data_load)
    a=to_mysql.Mysql('calls',data.data_load)
    a.write()
    print('ok')

def order():
    data = cd.Data(rw.r_csv('data/order.csv', ',', 0))
    data.order_form()
    data.data = data.data.sort_values(by=['phone']).reset_index(drop=True)
    data.remove_duplicates()
    data.data_to_load()
    print(data.data_load)
    a=to_mysql.Mysql('order',data.data_load)
    a.write()
    print('ok')

def popup():
    lang = ['data/popup_ua.csv','data/popup_ru.csv']
    for i in lang:
        data = cd.Data(rw.r_csv(i, ',', 0)) 
        data.popup_form(i)
        data.data = data.data.sort_values(by=['phone']).reset_index(drop=True)
        data.remove_duplicates()
        data.data_to_load()
        print(data.data_load)
        a=to_mysql.Mysql('popup',data.data_load)
        a.write()
        print('ok')

def client():
    data = rw.r_txt('data/ff.txt', 'zzzz', 0)
    data = data.drop([0,1,2,3,4,5]).reset_index(drop=True)
    for i in range(len(data)):
        data[0][i] = data[0][i].split('\t')
        data[0][i][0] = data[0][i][0].split(',')
        data[0][i][2] = data[0][i][2].replace('\xa0','').replace(',','.')
        data[0][i][1] = data[0][i][1].replace('\xa0','').replace(',','.')
    print(data)
    


if __name__ == '__main__':
    import timeit
    load = 'client'
    print(timeit.timeit(load+'()', setup="from __main__ import " + load,number=1))
