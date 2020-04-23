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

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("calls()", setup="from __main__ import calls",number=1))
