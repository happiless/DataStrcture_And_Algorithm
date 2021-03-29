/*************************************************************************
	> File Name: leetcode-25-K个一组翻转链表.cpp
	> Author: Happiless.zhang
	> Mail: ma6174@163.com 
	> Created Time: Tue 09 Mar 2021 05:41:56 PM CST
 ************************************************************************/

#include<iostream>
using namespace std;

class Solution {
public:
    ListNode *__reverseN(ListNode *head, int n) {
		if (n == 1) return head;
        ListNode *tail = head->next, *p = __reverseN(head->next, n - 1);
        head->next = tail->next;
        tail->next = head;
        return p;
    }
    ListNode *reverseN(ListNode *head, int n) {
        ListNode *p = head;
        int cnt = n;
        while (--n && p) p = p->next;
        if (p == nullptr) return head;
        return __reverseN(head, cnt);
    }

    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode ret(0, head), *p = &ret, *q = p->next;
        while ((p->next = reverseN(q, k)) != q) {
            p = q;
            q = p->next;
        }
        return ret.next;
    }
};
