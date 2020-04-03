import rw
import pandas as pd
import clean_data as cd
import to_mysql

tilda = rw.r_csv('./tilda.csv', ';', 0)
tilda = cd.Tilda(tilda) 
tilda.clean_data()
print(type(tilda.data['utm_medium'][0]))
a=to_mysql.Mysql('tilda',tilda.data)
a.write()
