import collections

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = collections.deque()
        queue.append([beginWord, 1])
        wordSet = set(wordList)

        while queue:
            word, steps = queue.popleft()

            if word == endWord:
                return steps

            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + ch + word[i+1:]
                    if newWord in wordSet:
                        wordSet.remove(newWord)
                        queue.append([newWord, steps + 1])
        
        return 0