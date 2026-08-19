from collections import deque
from typing import List


class Solution:
    def ladderLength(self, src: str, dst: str, wordList: List[str]) -> int:

        q = deque()
        q.append([src, 1])

        words = set()
        for i in range(len(wordList)): # fast searching
            words.add(wordList[i])

        while q:
            elements = q.popleft()
            word = elements[0]
            level = elements[1]

            if word == dst:
                return level
            # tc = number of words * word length * 26
            for i in range(len(word)):
                for alphabet in range(ord('a'), ord('z') + 1):
                    alphabet = chr(alphabet)

                    new_word = word[:i] + alphabet + word[i + 1:]

                    if new_word in words:
                        q.append([new_word, level + 1])
                        words.remove(new_word) #"I've already discovered this word using the shortest possible number of transformations. I don't need to process it again."

        return 0


if __name__ == "__main__":

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    sol = Solution()

    answer = sol.ladderLength(beginWord, endWord, wordList)

    print(answer)