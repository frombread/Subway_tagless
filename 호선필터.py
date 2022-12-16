import pandas as pd
df1 = pd.read_csv(r'C:\Users\user\Desktop\python workplace\TOP 60 호선.csv',encoding='utf-8-sig')
df2 = pd.read_csv(r'C:\Users\user\Desktop\python workplace\subway_line\8호선\8호선_대기업.csv',encoding='cp949')
#df2 = df2.dropna()
df2 = df2.drop(df2[df2['배포처'].isnull()].index, axis=0)
s = df2.groupby(['연번','호선','역명']).count()
s = s.reset_index()
s[['연번','호선','역명','역번호']]
s.rename(columns = {'역번호':'대기업'},inplace=True) ## 수정
a = s[['연번','호선','역명','대기업']] ## 수정
a.to_csv(r'C:\Users\user\Desktop\python workplace\주변8호선대기업.csv', encoding="utf-8-sig",index=False)
df1 = pd.read_csv(r'C:\Users\user\Desktop\python workplace\TOP 60 호선.csv',encoding='utf-8-sig')
df2 = pd.read_csv(r'C:\Users\user\Desktop\python workplace\주변8호선대기업.csv',encoding='utf-8-sig')
df1['연번'] = df1['연번'].astype(str)
df2['연번'] = df2['연번'].astype(str)
for i in df2.index:
    if len(df1[df1['연번']==df2.loc[i,'연번']]) ==True:
        in_de = df1[df1['연번']== (df2.loc[i,'연번'])].index
        df1.loc[in_de,'대기업'] = df2.loc[i,'대기업'] ## 수정
    else:
        pass
df1.to_csv(r'C:\Users\user\Desktop\python workplace\TOP 60 호선.csv', encoding="utf-8-sig",index=False)
