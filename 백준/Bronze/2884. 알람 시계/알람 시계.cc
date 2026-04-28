#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int main() {

	int hour, min;

	scanf("%d %d", &hour, &min);

	if (min >= 45) {
		printf("%d %d", hour, min - 45);
	}

	else if (min < 45) {
		if (hour == 0) {
			printf("23 %d", min + 15);
		}
		else
			printf("%d %d", hour - 1, min + 15);

	}

}