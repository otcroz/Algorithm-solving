#include <iostream>

using namespace std;

void quickSort(int i, int j, int* quick){
	if(i >= j) return;

	int temp;
	int pivot = quick[(i+j)] / 2;
	int left = i;
	int right = j;
	
	// ����, ������ Ȯ��
	 while(left <= right){

	 	while(quick[left] < pivot) left++;
	 	while(quick[right]> pivot) right--;
	 	if(left <= right){
	 		temp = quick[right];
	 		quick[right] = quick[left];
	 		quick[left] = temp;
	 		
	 		left++;
	 		right--;
		 }
	 }

	 // ���� left > right
	  quickSort(i, right, quick);
	  quickSort(left, j, quick);
}



int main(){
	// �ӽ� ������
	// ���Ŀ� �迭 ũ�� �ް� Radom���� �迭 ä���(�ڵ� ���� �ʿ�)
	int quick[5] = {5, 6, 3, 2, 1};
	
	

	for(int i=0; i< 5; i++){ 
		cout << quick[i] << "\n";
	}
	// ���� ������ ����, �ڵ� Ȯ�� �ʿ� 
	quickSort(0, 4, quick);
	
	for(int i=0; i< 5; i++){ 
		cout << quick[i] << "\n";
	}
	
	return 0;
} 
