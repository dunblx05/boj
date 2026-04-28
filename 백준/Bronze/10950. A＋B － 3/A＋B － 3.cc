#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int main() {
	int t;
	int a[100] = { 0 }, b[100] = { 0 };
	scanf("%d", &t);

	for (int i = 0; i < t; i++) {
		scanf("%d %d", &a[i], &b[i]);
	}

	for (int i = 0; i < t; i++) {
		printf("%d\n", a[i] + b[i]);
	}
}