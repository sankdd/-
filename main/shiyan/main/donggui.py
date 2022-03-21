import time

def donggui(N, V, v, w):

    start = time.perf_counter()


    f = [0] * (V + 1)
    for i in range(1, N+1):
        for j in range(V, v[i]-1,-1):
            f[j] = max(f[j], f[j-v[i]]+w[i])


    end = time.perf_counter()

    print("使用动态规划算法所得的解为{:d},运行时间为{:2f}s;".format(f[V], (end - start)))

    s = "使用动态规划算法所得的解为{:d},运行时间为{:2f}s;".format(f[V], (end - start)) + "\n"
    file = open('data/txt/donggui.txt', 'w')
    file.write(s)
    file.close()
