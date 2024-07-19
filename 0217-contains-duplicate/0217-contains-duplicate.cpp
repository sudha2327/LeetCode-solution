class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        map<int,int> dup;
	for(auto i : nums) {
		if(dup.find(i) != dup.end()) {
			return true;
		} else {
			dup[i]++;
		}
	}
	return false;
    }
};