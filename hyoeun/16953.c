#include <stdio.h>

int main() {
	int num1, num2, count = 1;
	scanf_s("%d%d", &num1, &num2);
	while (num1 < num2) {
		if (num2 % 10 == 1) {
			num2 = num2 / 10;
			count++;
		}
		else if (num2 % 2 == 0) {
			num2 = num2 / 2;
			count++;
		}
		else {
			break;
		}
	}
	if (num1 == num2) {
		printf("%d", count);
	}
	else {
		printf("-1");
	}
}
