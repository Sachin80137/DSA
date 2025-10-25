class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& mat) {
        int m = mat.size(), n = mat[0].size();
        int S_row = 0, S_col = 0, E_row = m-1, E_col = n-1;
        vector<int> ans;

        while(S_row <= E_row && S_col <= E_col){
            for(int j = S_col; j<=E_col; j++){
                ans.push_back(mat[S_row][j]);

            }
            for(int i=S_row+1; i<=E_row; i++){
                ans.push_back(mat[i][E_col]);
            }
            for(int j=E_col-1; j>=S_col; j--){
                if(S_row == E_row){
                    break;
                }
                ans.push_back(mat[E_row][j]);
            }
            for(int i=E_row-1; i>=S_row+1; i--){
                if(S_col == E_col){
                    break;
                }
                ans.push_back(mat[i][S_col]);
                
            }
            S_row++; E_row--; S_col++; E_col--;
        }
        return ans;

    }
};