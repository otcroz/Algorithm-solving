#include <iostream>
#include <cmath>
using namespace std;


void hanoi(int num, int start, int end, int mid) {
	if (num == 1) {
		cout << start << " " << end << "\n";
	}
	else {
		hanoi(num - 1, start, mid, end); // n-1 개의 원반 이동
		cout << start << " " << end << "\n";
		hanoi(num - 1, mid, end, start); // n-1 개의 원반 이동
	}
}

int main() {
	int num;

	// 값 입력받기
	cin >> num;

	// 이동 횟수
	cout << (int)pow(2, num) - 1 << "\n";
	// (1 << num) == (int)pow(2, num)
	
	hanoi(num, 1, 3, 2); // 원판 개수, 시작 장대, 끝 장대, 거쳐가는 장대

	return 0;
}