

class CheckDivisibility {

    static public boolean checkDivisibility(int n) {
        int sum = 0;
        int product = 1;
        int value = n;

        while (value > 0) {
            int digit = value % 10;
            sum += digit;
            product *= digit;
            value /= 10;
        }

        return n % (sum + product) == 0;
    }
    public static void main(String[] args) {
        int n = 99;
        System.err.println(checkDivisibility(n));
    }
}