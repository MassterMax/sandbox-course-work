import numpy as np
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows
        arr = [[1]]
        for i in range(2, n + 1):
            arr.append([1] * i)
            for j in range(1, i - 1):
                arr[i - 1][j] = arr[i - 2][j - 1] + arr[i - 2][j]
        return arr


class AnotherSolution:
    def __init__(self, nums: List[int]):
        self.orig = nums
        self.copy = self.orig.copy()

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        Lol
        kek

         l


          l l
        1
        """
        return self.orig

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.

        Yes!
        As it is.
        """
        np.random.shuffle(self.copy)
        return self.copy
