/*************************************************************************
	> File Name: leetcode-142-环状链表2.cpp
	> Author: ma6174
	> Mail: ma6174@163.com 
	> Created Time: Tue 09 Mar 2021 05:21:01 PM CST
 ************************************************************************/

#include<iostream>
using namespace std;


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if (head == nullptr || head->next == nullptr) return nullptr;
        ListNode *p = head, *q = head;
        do {
            p = p->next;
            q = q->next->next;
        } while (p != q && q && q->next);
        if (p != q) return nullptr;
        p = head;
        while (p != q) {
            p = p->next;
            q = q->next;
       }
       return q;
    }
};
