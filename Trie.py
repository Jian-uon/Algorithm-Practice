# coding: utf-8
# hihocoder第二周: http://hihocoder.com/contest/hiho2/problem/1
# 膜一下大牛代码，太扎实了。。
import collections

class TrieNode:
    def __init__(self):
        self.nodes = collections.defaultdict(TrieNode)#这个初始化太牛了。。
        self.count = 1
        self.isword = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self,word):
        curr = self.root
        for char in word:
            if char in curr.nodes:
                curr.nodes[char].count+=1
            curr = curr.nodes[char]
        curr.isword = True

    def search(self,word):
        curr = self.root
        for char in word:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        return curr.isword

    def startWith(self,prefix):
        curr = self.root
        for char in prefix:
            if char not in curr.nodes:
                return 0
            curr = curr.nodes[char]
        return curr.count

trie = Trie()

if __name__ == '__main__':
     for i in xrange(input()):
         trie.add(raw_input())
     for i in xrange(input()):
         print trie.startWith(raw_input())
     print trie.nodes
        
