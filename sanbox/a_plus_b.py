from typing import List


def list_sum_plus_bias(arr: List[int], b):
    sm = sum(arr)
    return sm + b


arr = [1, 2, 3]
res = list_sum_plus_bias(arr, 6)
print(res)
