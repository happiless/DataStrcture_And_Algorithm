from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        """

        :param arr:
        :return:
        """
        max_val = len(arr)
        k_list = []
        while max_val > 1:
            max_idx = arr.index(max_val)
            if max_idx != max_val - 1:
                arr[: max_idx + 1] = arr[:max_idx + 1][::-1]
                k_list.append(max_idx + 1)
                arr[: max_val] = arr[: max_val][::-1]
                k_list.append(max_val)
            max_val -= 1
        return k_list
