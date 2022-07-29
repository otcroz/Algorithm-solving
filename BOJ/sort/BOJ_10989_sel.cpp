/*#include <iostream>
using namespace std;

int main() { // 선택 정렬

	int num, i, j = 0, min, index = 0, temp;
	int array[10] = {};

	cin >> num;

	for (i = 0; i < num; i++) {
		cin >> array[i];
	}

	for (i = 0; i < num; i++) {
		min = 100000001;
		for (j = i; j < num; j++) {
			if (min > array[j]) {
				min = array[j];
				index = j;
			}
		}
		temp = array[i];
		array[i] = array[index];
		array[index] = temp;
	}

	for (i = 0; i < num; i++) {
		cout << array[i];
	}

	return 0;
}*/