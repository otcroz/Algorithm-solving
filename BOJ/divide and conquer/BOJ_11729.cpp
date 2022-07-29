#include <iostream>
#include <cmath>
using namespace std;


void hanoi(int num, int start, int end, int mid) {
	if (num == 1) {
		cout << start << " " << end << "\n";
	}
	else {
		hanoi(num - 1, start, mid, end); // n-1 ���� ���� �̵�
		cout << start << " " << end << "\n";
		hanoi(num - 1, mid, end, start); // n-1 ���� ���� �̵�
	}
}

int main() {
	int num;

	// �� �Է¹ޱ�
	cin >> num;

	// �̵� Ƚ��
	cout << (int)pow(2, num) - 1 << "\n";
	// (1 << num) == (int)pow(2, num)
	
	hanoi(num, 1, 3, 2); // ���� ����, ���� ���, �� ���, ���İ��� ���

	return 0;
}