import time

def tanxin(N, V, v, w):

    start = time.perf_counter()


    r = [0] * (N+1)
    for i in range(1, N+1):
        r[i] = w[i] / v[i]

    for i in range(1, N):
        for j in range(i+1, N+1):
            if r[i] < r[j]:
                tmp_v = v[i]
                tmp_w = w[i]
                tmp_r = r[i]
                v[i] = v[j]
                w[i] = w[j]
                r[i] = r[j]
                v[j] = tmp_v
                w[j] = tmp_w
                r[j] = tmp_r

    res = 0
    for i in range(N, 0, -1):
        if v[i] <= V:
            res = res + int(r[i]*v[i])
            V -= v[i]


    end = time.perf_counter()

    print("贪心算法所得的解为{:d},运行时间为{:2f}s;".format(res, end - start))

    s = "贪心算法所得的解为{:d},运行时间为{:2f}s;".format(res, end - start) + "\n"
    file = open('data/txt/tanxin.txt', 'w')
    file.write(s)
    file.close()