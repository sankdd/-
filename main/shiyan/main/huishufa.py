import time

bestV = 0
currW = 0
currV = 0


def backtrack(v, w, c, n, x, i):
    global bestV, currV, currW
    if i >= n:
        if bestV < currV:
            bestV = currV
    else:
        if currW + w[i] <= c:
            x[i] = 1
            currW += w[i]
            currV += v[i]
            backtrack(v, w, c, n, x, i + 1)
            currW -= w[i]
            currV -= v[i]
        x[i] = 0
        backtrack(v, w, c, n, x, i + 1)


def huishufa(N, V, v, w):
    start = time.perf_counter()

    n = int(N)
    c = int(V)
    x = [0 for i in range(n)]

    backtrack(v, w, c, n, x, 0)

    end = time.perf_counter()

    print("回溯算法所得的解为{:d},运行时间为{:2f}s;".format(bestV, end - start))

    s = "回溯算法所得的解为{:d},运行时间为{:2f}s;".format(bestV, end - start) + "\n"
    file = open('data/txt/huishufa.txt', 'w')
    file.write(s)
    file.close()












