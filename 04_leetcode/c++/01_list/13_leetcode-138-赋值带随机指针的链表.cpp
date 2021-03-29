/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (head == nullptr) return nullptr;
        Node *p = head, *q, *new_head;
        while (p) {
            q = new Node(p->val);
            q->random = p->random;
            q->next = p->next;
            p->next = q;
            p = q->next;
        }
        p = head->next;
        while (p) {
            if (p->random) p->random = p->random->next;
            (p = p->next) && (p = p->next);
        }
        new_head = head->next;
        p = head;
        while (p) {
            q = p->next;
            p->next = q->next;
            if (p->next) q->next = p->next->next;
            p = p->next;
        }
        return new_head;
    }
};