from collections import defaultdict
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        letters = defaultdict(lambda: 0)

        for letter in tasks:
            letters[letter] += 1
        
        frequent = max(letters.values())
        total = sum(letters.values())
        others = total - frequent

        return n * max(0, frequent - others - 1) + len(tasks)