import java.util.Scanner;

public class SumRange {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Get start and end numbers from user
        System.out.print("Enter start number: ");
        int start = scanner.nextInt();

        System.out.print("Enter end number: ");
        int end = scanner.nextInt();

        // Initialize sum and counter
        int sum = 0;
        int i = start;

        // Use while loop to add all numbers from start to end
        while (i <= end) {
            sum += i;
            i++;
        }

        // Display result
        System.out.println("Sum of numbers from " + start + " to " + end + " = " + sum);

        scanner.close();
    }
}
