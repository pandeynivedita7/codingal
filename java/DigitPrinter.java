public class DigitPrinter {
    public static void main(String[] args) {

        int num = 345;//345%10=5

        while (num > 0) {
            // Get the last digit using mod
            int digit = num % 10;
            System.out.println(digit);

            // Remove the last digit
            num = num / 10;
        }
    }
}
