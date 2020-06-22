#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <iostream>
using namespace std;
class Solution {
	public:
	    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
	        vector<bool> res(candies.size(), false);
	        int greatest = 0;
	        int i = 0;
	        for (i = 0;i<candies.size();i++) {
	            if (candies[i] > greatest) {
	                greatest = candies[i];
	            }
	        }

	        for (i = 0; i < candies.size(); ++i)
	        {
	        	if(candies[i] + extraCandies >= greatest) {
	        		res[i] = true;
	        	}
	        }
	        return res;
	    }
};

int main()
{
	Solution* sol = new Solution();
	vector<int> candies;
	candies.push_back(4);
	candies.push_back(2);
	candies.push_back(1);
	candies.push_back(1);
	candies.push_back(2);
	// for(auto r: candies) {
	// 	cout << r <<endl;
	// }
	int extraCandies = 1;
	vector<bool> res = sol->kidsWithCandies(candies, extraCandies);
	for(auto r: res) {
		cout << r <<endl;
	}
	/* code */
	return 0;
}

