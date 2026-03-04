import java.util.Scanner;

public class AddFromSumToNum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter start (sum): ");
        int sum = sc.nextInt(); // starting number

        System.out.print("Enter end (num): ");
        int num = sc.nextInt(); // ending number

        int total = 0;

        while (sum <= num) {
            total = total + sum; // add current number
            sum++; // move to next number
        }

        System.out.println("Total = " + total);
        sc.close();
    }
}
