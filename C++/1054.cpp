#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <iostream>
#include <tuple>
#include <queue>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> rearrangeBarcodes(vector<int>& barcodes) {
        std::vector<int> res;
        unordered_map<int, int> freq;
        priority_queue<pair<int, int>> pq;
        for (int num: barcodes) {
        	freq[num] += 1;
        }
        for (unordered_map<int, int>::iterator it = freq.begin();it != freq.end();it++) {
        	pq.push(make_pair(it->second, it->first));
        }
        while(res.size() < barcodes.size()) {
        	pair<int, int> p = pq.top();
        	res.push_back(p.second);
        	pq.pop();
        	if (res.size() < barcodes.size()) {
        		pair<int, int> p2 = pq.top();
	        	res.push_back(p2.second);
	        	pq.pop();
	        	pq.push(make_pair(p.first - 1, p.second));
	        	pq.push(make_pair(p2.first - 1, p2.second));
        	}
        }
        
        return res;
    }
};

int main()
{
	Solution* sol = new Solution();
	std::vector<int> barcodes;
	barcodes.push_back(3);
	barcodes.push_back(1);
	barcodes.push_back(1);
	barcodes.push_back(1);
	barcodes.push_back(2);
	barcodes.push_back(3);
	barcodes.push_back(3);
	vector<int> res = sol->rearrangeBarcodes(barcodes);
	for (auto num: res) {
		cout << num << " ";
	}
	return 0;
}





