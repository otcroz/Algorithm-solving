#include <iostream>
#include <stdio.h> 
#include <algorithm> // pair  
#include <vector> // vector
using namespace std;

int value[10];

int main()
{
	int N, end, begin;

	vector<pair<int, int>> schedule;

	cin >> N ;
	
	for (int i = 0; i < N; i++)
	{
		cin >> begin >> end;
		schedule.push_back(make_pair(end, begin)); // 값을 make_pair(end,begin)으로 
	}
	
	sort(schedule.begin(), schedule.end()); // 정렬: 오름차순  
	
	int time = schedule[0].first;
	int count = 1;
	for (int i = 1 ;i < N; i++) 
	{
		if (time <= schedule[i].second) // 첫 번째 회의 종료 시점 <= 두 번째 회의 시작 시점  
		{
			count++;
			time = schedule[i].first;
		}
	}

	cout << count;
}