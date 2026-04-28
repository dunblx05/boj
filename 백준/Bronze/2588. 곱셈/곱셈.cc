#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int main() {
	int a, b;
	scanf("%d", &a);
	scanf("%d", &b);
	
	int b_1 = b % 10;
	printf("%d\n", a * b_1);

	int b_10 = (b % 100) / 10;
	printf("%d\n", a*b_10);

	int b_100 = b / 100;
	printf("%d\n", a*b_100);

	printf("%d", a*b);
}