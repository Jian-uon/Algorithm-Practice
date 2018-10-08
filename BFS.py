# coding: utf-8
# hihocoder - 第五周 
# BFS->减枝到O(n)  1.后无效性 2.重复子问题(记忆化) 3.状态转移方程
# 同样的算法。。。真是找不出来哪里写错了。。C++写得就没问题。。头大！
num = [[0]*100]*100
best = [[0]*100]*100

def run(n):
    best[0][0] = num[0][0]
    for i in xrange(1, n):
        for j in xrange(i+1):
            if j == 0:
                best[i][j] = best[i-1][j] + num[i][j] 
                continue;
            if j == i:
                best[i][j] = best[i-1][j-1] + num[i][j] 
                continue
            best[i][j] = max(best[i-1][j-1], best[i-1][j]) + num[i][j]  
        #print best[i]
    print max(best[n-1])


if __name__ == '__main__':
    n = input()
    for i in range(n):
        num[i] = map(int, raw_input().split(" ")) 
    run(n)
