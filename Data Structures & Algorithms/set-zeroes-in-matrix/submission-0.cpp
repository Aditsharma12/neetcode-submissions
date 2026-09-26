class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {

        int n = matrix.size();
        int m = matrix[0].size();

        vector<int> rows;
        vector<int> cols;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {

                if (matrix[i][j] == 0) {
                    rows.push_back(i);
                    cols.push_back(j);
                }
            }
        }
        for (int r : rows) {
            for (int j = 0; j < m; j++) {
                matrix[r][j] = 0;
            }
        }

        for (int c : cols) {
            for (int i = 0; i < n; i++) {
                matrix[i][c] = 0;
            }
        }
    }
};