public class PrintDigits {
    public static void main(String[] args) {
        int num = 345;

        while (num > 0) {
            // get the last digit using mod
            int digit = num % 10;
            System.out.println(digit);

            // remove the last digit using division
            num /= 10;
        }
    }
}
