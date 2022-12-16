import math
import pandas as pd
df = pd.read_csv(r'C:\Users\user\Desktop\python workplace\fin1~9.csv',encoding='utf-8-sig')

def fr(arrival_num,service_time,mac_num):
    S = mac_num-1
    sum_val1 = 0
    for n_fac in range(0,S+1):
        sum_val1 += (((arrival_num / service_time)**n_fac) / math.factorial(n_fac))
    Po_num = 1/(sum_val1+((arrival_num/service_time)**mac_num)/(math.factorial(mac_num)*
                                                                (1-(arrival_num/service_time)/(mac_num))))
    L1= (((arrival_num/service_time)**(mac_num+1))/((mac_num-(arrival_num/service_time))*
                                                    (math.factorial(mac_num-1)))*Po_num) + \
                                                        (arrival_num/service_time)
                                                        
    L1 = (((L1 -(arrival_num/service_time))/service_time)) * 60
    return L1

def cal(arrival_num,ma_num):
    div_pop = arrival_num / 1510
    sr = 37
    div_ma = ma_num / 2
    wa_time = fr(div_pop,sr,int(div_ma))
    return wa_time

col_list = range(12,19)

for s in df.index:
    ma_num = df.loc[s,'개찰구']
    arrive_time_list = df.iloc[s,12:].values
    arrive_time_list

    for index, arrival_num in zip(col_list,arrive_time_list):
        print(s)
        wa_time = cal(arrival_num,ma_num)
        df.iloc[s,index] = wa_time


df.to_csv(r'C:\Users\user\Desktop\python workplace\wait.csv',encoding='utf-8-sig')
