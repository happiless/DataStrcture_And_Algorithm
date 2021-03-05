/*************************************************************************
	> File Name: 1.if_else.cpp
	> Author: ma6174
	> Mail: ma6174@163.com 
	> Created Time: Fri 05 Mar 2021 10:04:06 AM CST
 ************************************************************************/

#include<iostream>
#include<stdio.h>
using namespace std;

int main(){
	int n;
	while(~scanf("%d", &n)){
		if (!n) {
			printf("FOOLISH\n");
		} else if (n < 60) {
			printf("FAIL\n");
		} else if (n < 75) {
			printf("MEDIUM\n");
		} else {
			printf("GOOD\n");
		}
	}
	return 0;
}
