/*************************************************************************
	> File Name: 04_EP45.cpp
	> Author: ma6174
	> Mail: ma6174@163.com 
	> Created Time: Tue 09 Mar 2021 04:42:03 PM CST
 ************************************************************************/

#include<iostream>
#include<stdio.h>
using namespace std;

long long Triangle (long long n) {
	return n * (n + 1) >> 1;
}

long long Pentagonal (long long n) {
	return n * (3 * n - 1) >> 1;
}

long long Heaxgonal (long long n) {
	return n * (2 * n -1);
}

long long binary_search (long long (*arr)(long long), long long n, long long x) {
	long long head = 1, tail = n, mid;
	while (head <= tail) {
		mid = (head + tail) >> 1;
		if (arr(mid) == x) return mid;
		if (arr(mid) < x) head = mid + 1;
		else tail = mid - 1;
	}
	return -1;
}

int main() {
	long long n = 143;
	while (1) {
		n++; 
		long long temp = Heaxgonal(n);
		if (binary_search(Triangle, temp, temp) == -1) continue;
		if (binary_search(Pentagonal, temp, temp) == -1) continue;
		printf("%lld\n", temp);
		break;
	}
	return 0;
}
