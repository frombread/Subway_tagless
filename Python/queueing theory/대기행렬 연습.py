import math
def fin(arrive_time,service_time):
    return(arrive_time/service_time)



def se (arrive_time,service_time,mac_num,fr_num):
    Lq= (arrive_time/service_time)**(mac_num+1)/(mac_num*math.factorial(mac_num)*((1-(arrive_time/(mac_num*service_time)))**2))*fr_num
    return Lq


def fr(arrive_time,service_time,mac_num):
    S = mac_num - 1
    n = range(0,S+1)
    sum_val1 = 0
    for n_fac in n:
        sum_val1 += (1 / math.factorial(n_fac)) * ((arrive_time / service_time)**n_fac)
    
    fr_num = 1/ (sum_val1 + (1 /((math.factorial(mac_num) * (1-(arrive_time/(mac_num*service_time)))))* (arrive_time / service_time) ** mac_num))
    se_num = se(arrive_time,service_time,mac_num,fr_num)
    fin_num = fin(arrive_time,service_time)
    fin_result = (se_num + fin_num) / arrive_time
    return fin_result


print(fr(593,150,26))
