import pandas as pd
import numpy as np
pd.options.display.float_format = '{:.3f}'.format
np.set_printoptions(suppress=True,precision=3)
df = pd.read_csv(r'C:\Users\user\Desktop\python workplace\5555555.csv',encoding='utf-8-sig')
df['총 기업수'] = 0
df['주변학교'] = 0


for i in df.index:
    df.loc[i,'총 기업수'] = df.loc[i,'대기업'] + df.loc[i,'벤처기업'] + df.loc[i,'수출입기업'] + df.loc[i,'코스닥상장기업'] + df.loc[i,'외부감사기업'] + df.loc[i,'외국인투자기업'] #+df.loc[i,'중소벤처'] +df.loc[i,'은행']
    df.loc[i,'주변학교'] = df.loc[i,'중학교'] + df.loc[i,'고등학교'] + df.loc[i,'대학교']

df = df.drop('대기업',1)
df = df.drop('벤처기업',1)
df = df.drop('수출입기업',1)
df = df.drop('코스닥상장기업',1)
df = df.drop('외부감사기업',1)
df = df.drop('외국인투자기업',1)
df = df.drop('중학교',1)
df = df.drop('고등학교',1)
df = df.drop('대학교',1)

df.to_csv(r'C:\Users\user\Desktop\python workplace\5555기업총합.csv', encoding="utf-8-sig",index=False)

