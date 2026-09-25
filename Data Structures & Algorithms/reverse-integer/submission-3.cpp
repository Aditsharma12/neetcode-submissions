class Solution {
public:
    int reverse(int x) {
        int rev = 0;

        while (x != 0) {
            int R = x % 10;
            x = x / 10;

            if (rev > 214748364 || 
                (rev == 214748364 && R > 7)) {
                return 0;
            }

            if (rev < -214748364 || 
                (rev == -214748364 && R < -8)) {
                return 0;
            }

            rev = rev * 10 + R;
        }

        return rev;
    }
};