import rw
import pandas as pd
import clean_data as cd
import to_mysql
import timeit

def test():
    tilda = rw.r_csv('./tilda.csv', ';', 0)
    tilda = cd.Tilda(tilda)
    tilda.form_phone_nuber()
    tilda.data = tilda.data.sort_values(by=['phone']).reset_index(drop=True)
    tilda.clean_data()
    #print(tilda.data_load)
    a=to_mysql.Mysql('tilda',tilda.data_load)
    a.write2()
    print('ok')

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test",number=1))