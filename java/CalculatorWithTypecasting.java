// CalculatorWithTypecasting.java
// Demonstrates arithmetic operations and typecasting in Java

public class CalculatorWithTypecasting {
    public static void main(String[] args) {
        // Step 1: Declare integer variables
        int num1 = 7;
        int num2 = 2;

        // Step 2: Perform basic arithmetic operations
        int sum = num1 + num2;
        int difference = num1 - num2;
        int product = num1 * num2;
        int integerDivision = num1 / num2; // integer division (truncates decimal part)

        // Step 3: Use typecasting for accurate division
        double preciseDivision = (double) num1 / num2;
        // Step 4: Display results
        System.out.println("=== Calculator with Typecasting ===");
        System.out.println("First number (int): " + num1);
        System.out.println("Second number (int): " + num2);
        System.out.println("-----------------------------------");
        System.out.println("Addition: " + sum);
        System.out.println("Subtraction: " + difference);
        System.out.println("Multiplication: " + product);
        System.out.println("Integer Division (int/int): " + integerDivision);
        System.out.println("Precise Division (after typecasting): " + preciseDivision);
    }
}
