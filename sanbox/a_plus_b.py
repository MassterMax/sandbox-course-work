from typing import List


def list_sum_plus_bias(arr: List[int], b):
    """
    Simple method to return sum of array elements + bias
    :param arr: elements
    :param b: bias
    :return: sum
    """
    sm = sum(arr)
    return sm + b


arr = [1, 2, 3]
res = list_sum_plus_bias(arr, 6)
print(res)
