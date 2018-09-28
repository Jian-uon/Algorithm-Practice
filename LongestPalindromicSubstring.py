# coding: utf-8
# hihocoder第一周: http://hihocoder.com/contest/hiho1/problem/1
#1. O(n^3) 枚举所有字串
#2. O(n^2) 枚举字串中心,再枚举字串长度
#3. O(n) Manacher算法
#arr = "abacbacbacbcab"
def Manacher():
    arr = raw_input()
    new_arr = "#"
    longest_p_center = 0
    longest_p_right = 0
    start = 0
    maxlen = 0
    for i in xrange(len(arr)):
        new_arr += arr[i] + "#"
    length = [0]*(len(new_arr))

    for i in range(1, len(new_arr)):
        j = longest_p_center - (i - longest_p_center)
        if i < longest_p_right:
            length[i] = min(length[j], longest_p_right-i)
        else:
            length[i] = 1 
        while i + length[i] < len(new_arr) and i - length[i] > 0 and new_arr[i+length[i]] == new_arr[i-length[i]]:
            length[i] += 1
        if i + length[i] > longest_p_right:
            longest_p_right = i + length[i]
            lengest_p_center = i
        if length[i] > maxlen:
            maxlen = length[i]
            start = i
    print len(new_arr[start-maxlen+1:start+maxlen].replace("#", ''))

if __name__ == '__main__':
    for i in xrange(input()):
        Manacher()
#难道是因为后来才添加的python。。之前的题目就没跑时间？
