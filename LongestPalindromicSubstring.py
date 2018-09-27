# coding: utf-8
# hihocoder第一周: http://hihocoder.com/contest/hiho1/problem/1
#1. O(n^3) 枚举所有字串
#2. O(n^2) 枚举字串中心,再枚举字串长度
#3. O(n) Manacher算法
#arr = "abacbacbacbcab"
def GO():
    arr = raw_input()
    length = [0]*(len(arr)*2+1)
    new_arr = "#"
    longest_p_center = 0
    longest_p_right = 0
    start = 0
    maxlen = 0
    for i in xrange(len(arr)):
        new_arr += arr[i] + "#"
    for i in xrange(len(new_arr)):
        j = longest_p_center - (i - longest_p_center)
        if i <= longest_p_right:
            if i + length[j] < longest_p_right:
                length[i] = min(length[j], longest_p_right-i)
            else:
                length[i] = 1 
                while i + length[i] < len(new_arr) and i - length[i] > 0 and new_arr[i+length[i]] == new_arr[i-length[i]]:
                    length[i] += 1
            if i + length[i] > longest_p_right:
                longest_p_right = i + length[i]
                lengest_p_center = i
            if length[i] > maxlen:
                start = i
                maxlen = length[i]
    ans = ""
    for i in xrange(len(new_arr)):
        if i >= start - maxlen + 1 and i <= start+maxlen:
            ans += new_arr[i]
    ans = ans.replace('#', '')
    print len(ans) 

if __name__ == '__main__':
    for i in xrange(input()):
        GO()
#难道是因为后来才添加的python。。之前的题目就没跑时间？
