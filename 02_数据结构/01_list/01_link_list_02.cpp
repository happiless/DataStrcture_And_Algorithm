/*************************************************************************
	> File Name: 01_link_list_02.cpp
	> Author: ma6174
	> Mail: ma6174@163.com 
	> Created Time: Fri 05 Mar 2021 11:38:33 AM CST
 ************************************************************************/

#include<iostream>
#include<stdio.h>
using namespace std;

int data[10];
int next[10];

void add(int ind, int p, int val) {
	next[ind] = p;
	data[p] = val;
	return ;
}

int main() {
	int head = 3;
	data[3] = 0;
	add(3, 5, 1);
	add(5, 2, 2);
	add(2, 7, 3);
	add(7, 9, 100);
	int p = head;
	while (p != 0) {
		printf("%d->", data[p]);
		p = next[p];
	}
	printf("\n");

	return 0;
}
