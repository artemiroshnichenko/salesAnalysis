import rw
import pandas as pd
import clean_data as cd
import to_mysql


def tilda():
    data = cd.Tilda(rw.r_csv('data/tilda.csv', ';', 0)) #заносим фид в класс
    #data.tilda_form() #чистим данные
    #data.tilda_load() #формируем данные для загрузки
    #data.data_load = data.data_load.sort_values(by=['id']).reset_index(drop=True) #сортировка
    #data.remove_duplicates() #удаление дублей
    #print(data.data)
    print(data.data)
    #a=to_mysql.Mysql('tilda',data.data_load)
    #a.write()

    print('ok')
    #return data.data_load

def calls():
    data = cd.Data(rw.r_csv('data/call.csv', ',', 0))
    data.calls_form()
    data.data = data.data.sort_values(by=['phone']).reset_index(drop=True)
    data.remove_duplicates()
    data.data_to_load()
    #print(data.data_load)
    a=to_mysql.Mysql('lead',data.data_load)
    a.write()
    print('ok')


def order():
    data = cd.Data(rw.r_csv('data/order.csv', ',', 0))
    data.order_form()
    data.data = data.data.sort_values(by=['phone']).reset_index(drop=True)
    data.remove_duplicates()
    data.data_to_load()
    #print(data.data_load)
    a=to_mysql.Mysql('lead',data.data_load)
    a.write()
    print('ok')


def popup():
    lang = ['data/popup_ua.csv','data/popup_ru.csv']
    v = pd.DataFrame()
    for i in lang:
        data = rw.r_csv(i, ',', 0)
        data.rename(columns={'tel-749': 'phone', 'tel-853': 'phone', 'text-635': 'name', 'Date': 'date'}, inplace=True)
        v = pd.concat([v, data], ignore_index=True)
    data = cd.Data(v)
    data.popup_form()
    return data.data_load

def client():
    data = rw.r_txt('data/june.txt', 'zzz', 0)
    data = data.drop([0,1,2,3,4,5]).reset_index(drop=True)
    data = cd.Data(data)
    data.client_form()
    return data.data_load

def check(c_data,data):
    c_data['utm'] = ''
    for i in range(len(c_data)):
        for j in range(len(data)):
            if c_data['id'][i] == data['id'][j]:
                if data['utm_source'][j] != '':
                    c_data['utm'][i] = 1
                else:
                    c_data['utm'][i] = 'ads'
    return c_data

def main():
    #order()
    #popup()
    #calls()
    #tilda()
    #data = client()
    #sql = to_mysql.Mysql('lead', data)
    #sql.read()
    #print(sql.data)
    #rw.w_csv('data/res.csv',sql.data)
    tilda()
    #c = client()
    #res = check(c, t)
    #rw.w_csv('data/res.csv',res)


if __name__ == '__main__':
    import timeit
    load = 'main'
    print(timeit.timeit(load+'()', setup="from __main__ import " + load,number=1))
