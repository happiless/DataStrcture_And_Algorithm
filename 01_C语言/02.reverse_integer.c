/*************************************************************************
	> File Name: 2.reverse_integer.c
	> Author: ma6174
	> Mail: ma6174@163.com 
	> Created Time: Fri 05 Mar 2021 10:11:37 AM CST
 ************************************************************************/

#include<stdio.h>
using namespace std;

bool isPalindrome(int x) {
	if (__builtin_expect(!!(x < 0), 0)) return false;
	int y=0, z=x;
	while (x) {
		y = y*10 + x%10;
		x /= 10;
	}
	return y == z;
}

int main(){
	bool x;
	int n;
	while (~scanf("%d", &n)) {
		x = isPalindrome(n);
		if (x) {
			printf("%2d 是回文数字", n);
		} else {
			printf("%2d 不是回文数字", n);
		}
	}
	return 0;
}

