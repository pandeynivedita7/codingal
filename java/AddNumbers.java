import java.util.Scanner;

public class AddNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Ask user how many numbers to add
        System.out.print("How many numbers do you want to add? ");
        int count = scanner.nextInt();// 2

        int sum = 0;

        // Get numbers from user and add them
        for (int i = 1; i <= count; i++) {
            System.out.print("Enter number " + i + ": ");
            int num = scanner.nextInt();// 2
            sum += num;
        }

        // Display result
        System.out.println("Sum = " + sum);

        scanner.close();
    }
}