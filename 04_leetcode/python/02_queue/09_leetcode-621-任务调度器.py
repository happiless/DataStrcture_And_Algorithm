from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count_list = [0 for _ in range(26)]
        for task in tasks:
            count_list[ord(task) - ord('A')] += 1
        List.sort(count_list)
        max_count = 0
        for i in range(len(count_list)):
            print(count_list[len(count_list) - 1 - i])
            if count_list[25] == count_list[len(count_list) - 1 - i]:
                max_count += 1
            else:
                break
        print(max_count)
        return max(len(tasks), (count_list[25] - 1) * (n + 1) + max_count)

if __name__ == '__main__':
    print(Solution().leastInterval( ["A","A","A", 'A',"B","B","B"], 2))