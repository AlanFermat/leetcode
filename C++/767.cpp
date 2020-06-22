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
    string reorganizeString(string S) {
        priority_queue<pair<int, char>> pq;
        unordered_map<char, int> um;
        for (int i =0;i<S.size();i++) {
        	um[S[i]] += 1;
        	if (um[S[i]] > (S.size() + 1)/ 2) {
        		return "";
        	}
        }
        for (unordered_map<char, int>::iterator it = um.begin();it != um.end();it++) {
        	pq.push(make_pair(it->second, it->first));
        }
        string res = "";
        while (res.size() < S.size()) {
        	pair<int, char> p = pq.top();
        	// cout << p.first << " " << p.second << endl;
        	res += p.second;
        	pq.pop();
        	if (res.size() < S.size()) {
        		pair<int, char> p2 = pq.top();
        		res += p2.second;
        		pq.pop();
        		// cout << res <<" debug" << endl;
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
	cout << sol->reorganizeString("aabbbcc") << endl;
	return 0;
}
