#coding:utf-8
#http://hihocoder.com/contest/hiho7/problem/1
#完全背包。。
n, m = map(int, raw_input().split(' '))
val = [0]*100010
need = [0]*100010
dp = [0]*100010
for i in xrange(n):
    need[i], val[i] = map(int, raw_input().split(' '))

for i in xrange(n):
    for j in xrange(need[i], m+1):
        dp[j] = max(dp[j], dp[j-need[i]]+ val[i])

print dp[m]


