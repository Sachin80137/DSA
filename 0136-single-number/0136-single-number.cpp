class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans =0;
        for(int val: nums){
            ans = ans ^ val;
            //OR we use XOR,    ans ^= val;
            //ans ^= val;
        }
        return ans;
        
    }
};