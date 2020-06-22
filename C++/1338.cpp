#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <iostream>
#include <queue> 
#include <utility> 
#include <unordered_map>
using namespace std;


/// Using pq ///
// auto compare = [](pair<int, int> a, pair<int, int> b) { 
// 	if (a.first == b.first) {
// 		return a.second < b.second;
// 	} else {
// 		return a.first < b.first;
// 	}
// };

// class Solution {
// public:

// 	void showpq(priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(compare)> pq) {
// 		priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(compare)> myPq = pq;
// 		while(!myPq.empty()) {
// 			cout << "pair (" << (myPq.top()).first << ", " << (myPq.top()).second << ")" << endl;
// 			myPq.pop();
// 		}
// 	}

//     int minSetSize(vector<int>& arr) {
//         int neededLen = arr.size() / 2;
//         if (neededLen == 0) {
//         	return 0;
//         }
//         if (neededLen == 1) {
//         	return 1;
//         }
//         int setSize = 0;
        
//         priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(compare)> pq(compare);
       
       
//         unordered_map<int, int> keyToCnt;
//         for (int num: arr)
//         {
//         	keyToCnt[num] = keyToCnt[num] + 1;
//         }
//         for (auto it = keyToCnt.begin(); it != keyToCnt.end();it++) {
//         	pq.push(make_pair(it->second, it->first));
//         }
//         showpq(pq);

//         while(neededLen > 0) {
//         	neededLen -= (pq.top()).first;
//         	pq.pop();
//         	setSize++;
//         }
//         return setSize;
//     }
// };


/// Using bucked sort ///
class Solution
{
public:
	int minSetSize(vector<int>& arr) {
		int setSize = 0;
		int neededLen = arr.size() / 2;
		if (neededLen <= 1) {
			return neededLen;
		}

		vector<int> bucked(100001, 0);
		unordered_map<int, int> keyToCnt;
		for (int num: arr) {
        	keyToCnt[num] = keyToCnt[num] + 1;
        }
        for (auto it = keyToCnt.begin(); it != keyToCnt.end();it++) {
        	bucked[it->second] ++;
        }

        int i =0;
        bool flag = true;
        for (i=100000;i>0;i--) {
        	while (bucked[i]) {
        		neededLen -= i;
        		bucked[i] --;
        		setSize++;
        		if(neededLen <= 0) {
        			flag = false;
        			break;
        		}
        	}
        	if (! flag) {
        		break;
        	}
        }
        return setSize;
	}
	
};

int main()
{
	Solution* sol = new Solution();
	std::vector<int> arr;
	arr.push_back(3);
	arr.push_back(3);
	arr.push_back(3);
	arr.push_back(3);
	arr.push_back(5);
	arr.push_back(5);
	arr.push_back(5);
	arr.push_back(2);
	arr.push_back(2);
	arr.push_back(7);
	int res = sol->minSetSize(arr);
	cout << "result is " << res << endl;
	return 0;
}

