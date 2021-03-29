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
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == nullptr) return nullptr;
        int cnt = 1;
        ListNode *p = head;
        while (p->next) p = p->next, cnt ++;
        p->next = head;
        k %= cnt;
        k = cnt - k;
        while (k--){
            p = p->next;
        }
        head = p->next;
        p->next = nullptr;
        return head;
    }
};