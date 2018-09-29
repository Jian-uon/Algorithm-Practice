#coding:utf-8
#http://hihocoder.com/contest/hiho3/problem/1
#KMP算法
#又是TLE......

def cal_next(pattern):
    nxt = [0 for _ in xrange(len(pattern))]
    nxt[0] = -1
    k = -1
    for i in xrange(1, len(pattern)):
        while k > -1 and pattern[k+1] != pattern[i]:
            k = nxt[k]
        if pattern[k+1] == pattern[i]:
            k += 1
        nxt[i] = k
    #print nxt 
    return nxt

def KMP(oriStr, pat):
    p = -1
    ans = 0
    i = 0
    next = cal_next(pat)
    while i < len(oriStr):
        while p > -1 and oriStr[i] != pat[p+1]:
            p = next[p]
        if oriStr[i] == pat[p+1]:
            p += 1
        if p == len(pat)-1:
           p = -1 
           i -= 1
           ans += 1 
        i += 1
    return ans 

if __name__ == '__main__':
    n = input()
    for i in xrange(n):
        pat = raw_input()
        ori = raw_input()
        print KMP(ori, pat)
