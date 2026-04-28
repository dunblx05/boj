#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
	int n;
	int cnt = 0, num = 0;
	scanf("%d", &n);

	while (cnt != n) {
		num++;
		int temp = num;
		while (temp != 0) {
			if (temp % 1000 == 666) {
				cnt++;
				break;
			}
			else
				temp = temp / 10;
		}
	}
	printf("%d", num);

}