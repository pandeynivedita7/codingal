// VariableManipulation.java
// Demonstrates basic variable manipulation in Java

public class VariableManipulation {
    public static void main(String[] args) {
        // Step 1: Declare and initialize variables
        int apples = 10;
        double pricePerApple = 0.75;
        char n = 'v';
        boolean is_student = true;
        String owner = "Emma";

        // Step 2: Display initial values
        System.out.println("Owner: " + owner);
        System.out.println("Apples: " + apples);
        System.out.println("Price per apple: $" + pricePerApple);
        System.out.println("char, " + n);
        System.out.println(("is_student, " + is_student));

        // Step 3: Manipulate variables
        apples = apples + 5; // Emma buys 5 more apples
        pricePerApple = pricePerApple * 1.10; // Price increases by 10%

        // Step 4: Calculate total cost
        double totalCost = apples * pricePerApple;

        // Step 5: Display new values
        System.out.println("\nAfter buying more apples and price change:");
        System.out.println("Updated apples: " + apples);
        System.out.println("New price per apple: $" + pricePerApple);
        System.out.println("Total cost: $" + totalCost);

    }
}
