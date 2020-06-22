#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <iostream>
#include <tuple>
using namespace std;
class Solution {
public:
	vector<int> findDiagonalOrder(vector<vector<int>>& nums) {
		vector<int> res;
		vector<tuple<int, int, int>> to_be_sorted;
		int i = 0;
		int j = 0;
		for (i=0;i< (int)nums.size();i++) {
			int length = nums[i].size();
			for (j=0;j< length;j++) {
				to_be_sorted.push_back(make_tuple(i+j, -i, nums[i][j]));
			}
		}

		sort(to_be_sorted.begin(), to_be_sorted.end(), [](tuple<int, int, int> &a, tuple<int, int, int> &b){
			int a_summ = get<0>(a);
			int b_summ = get<0>(b);
			if (a_summ == b_summ) {
				return get<1>(a) < get<1>(b);
			}
			return a_summ < b_summ;
		});

		for (auto t:to_be_sorted) {
			res.push_back(get<2>(t));
		}
		return res;
	}
};

void printVectors(vector<vector<int>>& nums) {
	for (auto v:nums) {
		for (auto num: v) {
			cout << num << " ";
		}
		cout << "" << endl;
	}
}

void printAVector(vector<int>& v) {
	for (auto num: v) {
		cout << num << " ";
	}
}

int main()
{
	Solution* sol = new Solution();
	vector<vector<int>> nums;
	vector<int> num1;
	num1.push_back(1);
	num1.push_back(2);
	num1.push_back(3);
	vector<int> num2;
	num2.push_back(4);
	num2.push_back(5);
	num2.push_back(6);
	vector<int> num3;
	num3.push_back(7);
	num3.push_back(8);
	num3.push_back(9);
	nums.push_back(num1);
	nums.push_back(num2);
	nums.push_back(num3);
	std::vector<int> res = sol->findDiagonalOrder(nums);
	printAVector(res);
	return 0;
}

