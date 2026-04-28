#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {

	int n;
	int cnt = 0;
	int result = 0;
	int n_10, n_1, sum, nn;
	scanf("%d", &n);
	result = n;

	while (1) {
		n_10 = n / 10;
		n_1 = n % 10;
		sum = n_10 + n_1;
		nn = (n_1 * 10) + (sum % 10);
		n = nn;
		cnt = cnt + 1;

		if (nn == result) break;
	}
	printf("%d", cnt);
	return 0;
}