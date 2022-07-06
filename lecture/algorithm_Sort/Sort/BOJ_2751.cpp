#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int number, data[1000001];

void quicksort(int* data, int start, int end) {
	if (start >= end) return;

	int key = start;
	int i = start + 1, j = end, temp;
	while (i <= j) {
		while (data[i] <= data[key]) {
			i++;
		}
		while (data[j] >= data[key] && j > start) { // j가 왼쪽에 있는 값을 침범하지 못하도록
			j--;
		}
		if (i > j) { // pivot과 바꾸어줌
			temp = data[j];
			data[j] = data[key];
			data[key] = temp;
		}
		else { 
			temp = data[i];
			data[i] = data[j];
			data[j]= temp;
		}
	}
	quicksort(data, start, j - 1);
	quicksort(data, j + 1, end);
}

int main() {
	scanf("%d ", &number);
	for (int i = 0; i < number; i++) {
		scanf("%d", &data[i]);
	}

	quicksort(data, 0, number - 1);

	for (int i = 0; i < number; i++) {
		printf("%d ", data[i]);
	}

	return 0;
}