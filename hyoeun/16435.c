#include <stdio.h>

int main() {
	//선언할 변수 : snake 길이, 과일 갯수, 과일 높이
	int snakeLength, countFruit, save = 0;
	int highFruit[1000];
	int n = 0;
	scanf_s("%d", &countFruit);
	scanf_s("%d", &snakeLength);
	for (int i = 0; i < countFruit; i++) {
		scanf_s("%d", &highFruit[i]);
	}
	for (int i = 0; i < countFruit; i++) {
		for (int j = 0; j < countFruit - 1; j++) {
			if (highFruit[j] > highFruit[j + 1]) {
				save = highFruit[j];
				highFruit[j] = highFruit[j + 1];
				highFruit[j + 1] = save;
			}
		}
	}
	for (int j = 0; j < countFruit; j++) {//스네이크 과일 갯수만큼 반복(먹으면 길이 늘리고 먹지 못하면 종료 후 길이 출력)
		if (snakeLength >= highFruit[j])
			snakeLength++;
	}
	printf("%d", snakeLength);
	return 0;
}