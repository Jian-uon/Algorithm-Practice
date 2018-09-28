trie = {}
def insert(word):
    global trie 
    root = trie
    for i in word:
        if i not in root:
            root[i] = [0, {}]
        root[i][0] += 1
        root = root[i][1]

def startWith(word):
    global trie 
    root = trie
    ans = 0
    isEnd = 0
    for i in word:
        if i not in root:
            break
        else:
            isEnd += 1
            if isEnd == len(word):
                ans = root[i][0]
            root = root[i][1]
    return ans
    #本来想写成root[len-1][0]的形式,发现搜索的过程是不可逆的

if __name__ == '__main__':
    for i in xrange(input()):
        insert(raw_input())
    for i in xrange(input()):
        print startWith(raw_input())
