#include <stdio.h>

int main() {
	int JOI, money = 1000, pay, dongjeon[6] = { 500,100,50,10,5,1 };
	int count = 0;
	scanf_s("%d", &JOI);
	pay = money - JOI;
	for (int i = 0; i < 6; i++) {
		count = count + (pay / dongjeon[i]);
		pay = pay % dongjeon[i];
	}
	printf("%d", count);
	return 0;
}