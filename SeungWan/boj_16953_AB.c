#include <stdio.h>
 
int main() {
    int a, b;
	scanf("%d %d",&a ,&b);
	int cnt = 0;
	while (1) {
		if (a > b) {
			printf("-1");
			break;
		}
		if (a == b) {
			printf("%d", cnt + 1);
			break;
		}
 
		if (b % 10 == 1) {
			b /= 10;
		}
		else if (b % 2 == 0) {
			b /= 2;
		}
		else {
			printf("-1");
			break;
		}
		cnt++;
	}
	return 0;
}
