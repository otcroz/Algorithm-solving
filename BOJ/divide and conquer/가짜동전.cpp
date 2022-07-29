#include <iostream>

using namespace std;

void quickSort(int i, int j, int* quick){
	if(i >= j) return;

	int temp;
	int pivot = quick[(i+j)] / 2;
	int left = i;
	int right = j;
	
	// 왼쪽, 오른쪽 확인
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

	 // 이제 left > right
	  quickSort(i, right, quick);
	  quickSort(left, j, quick);
}



int main(){
	// 임시 데이터
	// 추후에 배열 크기 받고 Radom으로 배열 채우기(코드 수정 필요)
	int quick[5] = {5, 6, 3, 2, 1};
	
	

	for(int i=0; i< 5; i++){ 
		cout << quick[i] << "\n";
	}
	// 무한 루프에 빠짐, 코드 확인 필요 
	quickSort(0, 4, quick);
	
	for(int i=0; i< 5; i++){ 
		cout << quick[i] << "\n";
	}
	
	return 0;
} 
