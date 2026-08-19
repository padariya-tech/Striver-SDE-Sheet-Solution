from collections import deque
from typing import List


class Solution:
    def ladderLength(self, src: str, dst: str, wordList: List[str]) -> int:

        q = deque()
        q.append([src,[src]])

        words = set(wordList)

        if dst not in words:
            return []
    
        ans = []

        while q:

            level_size = len(q)

            used_this_level = set()

            for _ in range(level_size):

                word,path = q.popleft()

                if word == dst:
                    ans.append(path)
                    continue

                for i in range(len(word)):
                    for alphabet in range(ord('a'), ord('z') + 1):
                        alphabet = chr(alphabet)

                        new_word = word[:i] + alphabet + word[i + 1:]

                        if new_word in words:
                            q.append([
                                new_word,
                                path + [new_word]
                            ])
                            used_this_level.add(new_word)

            for word in used_this_level:
                words.remove(word)

            if ans:
                return ans
                        
        return []

if __name__ == "__main__":

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    sol = Solution()

    answer = sol.ladderLength(beginWord, endWord, wordList)

    print(answer)