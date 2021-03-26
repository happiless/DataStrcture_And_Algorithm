/*************************************************************************
	> File Name: 03.struct_program.c
	> Author: Happiless
	> Mail: ma6174@163.com 
	> Created Time: Tue 09 Mar 2021 04:13:58 PM CST
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<inttypes.h>

int rev_num(int n) {
	if (n < 0) return 0;
	int x = n, temp = 0;
	while (x) {
		temp = temp * 10 + x % 10;
		x /= 10;
	}
	return temp == n;
}

int srand_num (int n, int cnt) {
	srand(time(0));
	for (int i=0; i<n; i++) {
		int val = rand() % 100;
		i && printf(" ");
		printf("%d", val);
		cnt += (val & 1);
	}
	printf("\n");
	printf("cnt: %d\n", cnt);
}

int main(){
	int n, cnt = 0;
	printf("int32_max = %d\n", INT32_MAX);
	scanf("%d", &n);
	printf("%s\n", rev_num(n) ? "YES" : "NO");
	return 0;
}
