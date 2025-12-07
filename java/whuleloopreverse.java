class ReverseNumber {
    public static void main(String[] args) {

        int num = 12345;   // number to reverse
        int rev = 0;       // variable to store reversed number

        while (num != 0) {
            int digit = num % 10;     // extract last digit
            rev = rev * 10 + digit;   // add digit to reversed number
            num = num / 10;           // remove last digit
        }

        System.out.println("Reversed number: " + rev);
    }
}
