import rw
import pandas as pd
import clean_data as cd

tilda = rw.r_csv('./tilda.csv',';')
tilda = cd.Tilda(tilda)
print(tilda.data)
