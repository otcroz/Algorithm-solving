#include <iostream>
using namespace std;

int main() { // 버블 정렬

	int num, i, j = 0, index = 0, temp;
	int array[10] = {};

	cin >> num;

	for (i = 0; i < num; i++) {
		cin >> array[i];
	}

	for (i = 0; i < num; i++) {
		for (j = 0; j < (num-1) - i; j++) {
			if (array[j] > array[j + 1]) {
				temp = array[j];
				array[j] = array[j + 1];
				array[j + 1] = temp;

			}
		}
	}

	for (int i = 0; i < num; i++) {
		cout << array[i];
	}

	return 0;
}