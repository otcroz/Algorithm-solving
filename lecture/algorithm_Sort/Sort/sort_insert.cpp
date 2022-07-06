#include <stdio.h>

int main() {
	int i, j, temp;

	int array[10] = { 1,10,5,8,6,7,4,3,2,9 };

	for (int i = 0; i < 9; i++) {
		j = i;
		while (array[j] > array[j + 1]) { // 앞이 정렬되어 있다고 가정
			temp = array[j];
			array[j] = array[j+1];
			array[j+1] = temp;
			j--;
		}
	}
	for (int i = 0; i < 10; i++) {
		printf("%d ", array[i]);
	}
	return 0;
}