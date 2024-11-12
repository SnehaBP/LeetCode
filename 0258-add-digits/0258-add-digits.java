class Solution {
    public int addDigits(int num) {
        while (num >= 10) {
            num = sumDigits(num);
        }
        return num;
    }
    private int sumDigits(int n) {
        int sum = 0;
        while (n != 0) {
            sum += n % 10;
            n = n / 10;
        }
        return sum;
    }
}