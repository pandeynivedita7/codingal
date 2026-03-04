import java.util.Scanner;

public class DigitsWhile {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int num = sc.nextInt();

        while (num > 0) {
            // get the last digit using mod
            int digit = num % 10;
            System.out.println(digit);

            // remove the last digit
            num = num / 10; // integer division
        }

        sc.close();
    }
}
