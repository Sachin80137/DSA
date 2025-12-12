class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int n = nums.size();
        if(n==0) return 0;
        
        unordered_set<int> st;
        for(int i: nums) st.insert(i);

        int  globalLen = 0;
        for(int i: st){
            if(!st.count(i - 1)){
                int currLen = 1;
                int currNum = i;
                while(st.count(currNum +1)){
                    currLen ++;
                    currNum ++;
                }
                globalLen = max(currLen, globalLen);
            }
        }
        return globalLen;
        
    }
};