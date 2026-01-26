import java.util.Scanner;

public class SalmonSpawning {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Ask the user for the month number
        System.out.print("Enter the month (1–12): ");
        int month = sc.nextInt();

        // Check spawning season in numerical order
        if (month >= 4 && month <= 6) {
            System.out.println("Spring spawning season");
        } else if (month >= 10 && month <= 12) {
            System.out.println("Fall spawning season");
        } else {
            System.out.println("Not spawning season");
        }

        sc.close();
    }
}
