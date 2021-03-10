/*************************************************************************
	> File Name: leetcode-206.cpp
	> Author: Happiless.zhang
	> Mail: ma6174@163.com
	> Created Time: Fri 05 Mar 2021 02:29:18 PM CST
 ************************************************************************/

#include<iostream>
using namespace std;

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head == nullptr || head->next == nullptr) return head;
        ListNode *pre = nullptr;
        ListNode *cur = head;
        ListNode *p = head->next;
        while (cur) {
            cur->next = pre;
            pre = cur;
            (cur = p) && (p = p->next);
        }
        return pre;
    }
};