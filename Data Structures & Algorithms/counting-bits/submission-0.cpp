class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> k;
        for(int i=0;i<=n;i++)
        {
            int count=0;
            int x=i;
            while(x)
            {
                x=x&(x-1);
                count++;
            }
            k.push_back(count);
        }
        return k;
    }
};
