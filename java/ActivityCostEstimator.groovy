import java.util.Scanner;

public class ActivityCostEstimator {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        // Input in exact order
        System.out.print("Enter your brunch cost: ");
        double yourBrunch = input.nextDouble();

        System.out.print("Enter movie ticket cost per person: ");
        double movieCost = input.nextDouble();

        System.out.print("Enter your cake cost: ");
        double yourCake = input.nextDouble();

        // Friend's costs based on rules
        double friendBrunch = yourBrunch * 2;          // friend's entree twice your cost
        double friendMovie = movieCost;                // same movie ticket cost per person
        double friendCake = yourCake / 3;              // friend's cake costs 1/3 of yours

        // Totals per activity
        double totalBrunch = yourBrunch + friendBrunch;
        double totalMovie = movieCost + friendMovie;
        double totalCake = yourCake + friendCake;

        // Grand total
        double grandTotal = totalBrunch + totalMovie + totalCake;

        // Output
        System.out.println("Brunch total: $" + totalBrunch);
        System.out.println("Movie tickets total: $" + totalMovie);
        System.out.println("Cake total: $" + totalCake);
        System.out.println("Grand total for the day: $" + grandTotal);
    }
}
