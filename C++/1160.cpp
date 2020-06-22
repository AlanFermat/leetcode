#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <iostream>
#include <tuple>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {
        int res = 0;
        unordered_map<char, int> um;
        for (int i = 0;i<chars.size();i++) {
        	um[chars[i]] += 1;
        }
        for (auto word: words) {
        	int checked = 1;
        	unordered_map<char, int> temp = um;
        	for (int j =0;j<word.size();j++) {
        		if (temp[word[j]] < 1) {
        			checked = 0;
        			break;
        		}
        		temp[word[j]] -= 1;
        	}
        	if (checked) {
        		res += word.size();
        	}
        }
        return res;
    }
};

int main()
{
	Solution* sol = new Solution();
	std::vector<string> v;
	v.push_back("cat");
	v.push_back("bt");
	v.push_back("hat");
	v.push_back("thaaa");
	string chars = "atach";
	int res = sol->countCharacters(v, chars);
	cout << res << endl;
	return 0;
}