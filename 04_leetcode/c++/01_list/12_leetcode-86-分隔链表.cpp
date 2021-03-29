/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
    /**
     *
     *
     */
        ListNode r1, r2, *p1 = &r1, *p2 = &r2, *p = head, *q;
        while (p) {
            q = p->next;
            if (p->val < x) {
                p->next = nullptr;
                p1->next = p;
                p1 = p;
            } else {
                p->next = nullptr;
                p2->next = p;
                p2 = p;
            }
            p = q;
        }
        p1->next = r2.next;
        return r1.next;
    }
};