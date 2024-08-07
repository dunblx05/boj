#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <stdbool.h>

void queens(int i);
int promising(int i);
int n, count = 0;
int col[15] = { 0, };

int main() {
	scanf("%d", &n);
	queens(0);
	printf("%d", count);
}

void queens(int i) {
	int j;
	if (promising(i)) {
		if (i == n) {
			count++;
			
		}
		else {
			for (j = 1; j <= n; j++) {
				col[i + 1] = j;
				queens(i + 1);
			}
		}
	}
}

int promising(int i) {
	int k = 1, promise = 1;
	while (k < i && promise == 1) {
		if ((col[i] == col[k]) || abs(col[i] - col[k]) == abs(i - k)) {
			promise = 0;
		}
		k++;
	}
	return promise;
}