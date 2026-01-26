import java.util.Scanner;

public class ParkingGarage {
    public static void main(String[] args) {
        // Create Scanner object to read input
        Scanner sc = new Scanner(System.in);

        // Ask the user for number of hours parked
        System.out.print("Enter number of hours parked: ");
        double hours = sc.nextDouble();

        // Parking rate per hour
        double ratePerHour = 4.50;

        // Maximum charge
        double maxCharge = 30.0;

        // Calculate total cost
        double total = hours * ratePerHour;

        // Apply maximum charge rule
        if (total > maxCharge) {
            total = maxCharge;
        }

        // Display the total amount owed
        System.out.println("Total parking charge: $" + total);

        sc.close();
    }
}
