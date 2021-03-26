/*************************************************************************
	> File Name: 01_link_list.cpp
	> Author: ma6174
	> Mail: ma6174@163.com 
	> Created Time: Fri 05 Mar 2021 11:27:02 AM CST
 ************************************************************************/

#include<iostream>
#include<stdio.h>
using namespace std;

struct Node {
	Node(int data) : data(data), next(NULL) {}
	int data;
	Node *next;
};

Node *reverse(Node *head, int n) {
    if (n == 1) return head;
    Node *tail = head->next, *p = reverse(head->next, n - 1);
    head->next = tail->next;
    tail->next = head;
    return p;
}

int main() {
	Node *head = NULL;
	head = new Node(1);
	head->next = new Node(2);
	head->next->next = new Node(3);
	head->next->next->next = new Node(4);
	head = reverse(head, 2);
	Node *p = head;
	while (p != NULL) {
		printf("%d->", p->data);
		p = p->next;
	}
	printf("\n");
	return 0;
}
