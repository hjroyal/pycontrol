from matplotlib import pyplot as plt
import random

def PID(now_v,expc_v):
    Kp = 0.01
    Ki = 0
    Kd = 0
    sum_err = 0
    v_list = []
    err = expc_v - now_v
    err_last = err  # 上一次的输出,先初始化为一致
    cnt = 0
    while abs(err) > 0.001:  # 误差还在范围外
        err = expc_v - now_v
        sum_err += err
        uk = Kp*err + Ki * sum_err + Kd * (err-err_last) # 确定本次输出
        #now_v = now_v + uk + random.uniform(-0.1,0.1)  # 更新当前速度,加入一个扰动
        now_v = now_v + uk + random.uniform(-2,2)
        now_v = now_v + uk
        err_last = err
        v_list.append(now_v)
        cnt += 1
    print(cnt)
    plt.plot(v_list)
    plt.show()
 
if __name__ == '__main__':
    PID(60,100)