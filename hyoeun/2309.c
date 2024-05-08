#include <stdio.h>

int main() {
	int out1=0,out2=0,save,sum=0;
	int arr[9];
	for (int i = 0; i < 9; i++) {
		scanf_s("%d", &arr[i]);
		sum += arr[i];
	}
	sum -= 100;
	for (int j = 0; j < 8; j++) {
		for (int x = 0; x < 8-j; x++) {
			if (arr[x] > arr[x+1]) {
				save = arr[x+1];
				arr[x+1] = arr[x];
				arr[x] = save;
			}
		}
	}
	for (int o = 0; o < 9; o++) {
		for (int p = 0; p < 9; p++) {
			if (arr[o] != arr[p]) {
				if (arr[o] + arr[p] == sum) {
					out1 = arr[o];
					out2 = arr[p];
					break;
				}
			}
		}
			if (out1 != 0 && out2 != 0)
				break;
	}
	for (int q = 0; q < 9; q++) {
		if (arr[q] != out1 && arr[q] != out2)
			printf("%d\n", arr[q]);
	}
}