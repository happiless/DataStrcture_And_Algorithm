from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        twenty = 0
        for bill in bills:
            print(f'five: {five}')
            print(f'ten: {ten}')
            print(f'twenty: {twenty}')
            if bill == 5:
                five += 1
            elif bill == 10:
                ten += 1
                if five > 0:
                    five -= 1
                else:
                    return False
            else:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                    twenty += 1
                elif five >= 3:
                    five -= 3
                    twenty += 1
                else:
                    return False
        return True


if __name__ == '__main__':
    print(Solution().lemonadeChange([5,5,5,10,5,5,10,20,20,20]))