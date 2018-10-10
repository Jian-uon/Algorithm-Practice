#coding: utf-8
#http://hihocoder.com/contest/hiho6/problem/1


n, m = map(int, raw_input().split(" "))
val = [0]*(n+1)
need = [0]*(n+1)
dp = [0]*(m+1)
for i in xrange(n):
    need[i], val[i] = map(int, raw_input().split(" "))

for i in range(n):
    for j in range(m, need[i]-1, -1):
        dp[j] = max(dp[j], dp[j-need[i]] + val[i])
print dp[m]

