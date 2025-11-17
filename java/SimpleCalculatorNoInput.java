// SimpleCalculatorNoInput.java
// A basic calculator program without using Scanner

public class SimpleCalculatorNoInput {
    public static void main(String[] args) {
        // Step 1: Declare and initialize variables
        double num1 = 25.0;
        double num2 = 5.0;

        // Step 2: Perform arithmetic operations
        double sum = num1 + num2;
        double difference = num1 - num2;
        double product = num1 * num2;
        double quotient = num1 / num2;
        double modulus = num1 % num2;
        num1++;
        num2--;

        // Step 3: Display results
        System.out.println("=== Simple Calculator ===");
        System.out.println("First number: " + num1);
        System.out.println("Second number: " + num2);
        System.out.println("-------------------------");
        System.out.println("Addition: " + sum);
        System.out.println("Subtraction: " + difference);
        System.out.println("Multiplication: " + product);
        System.out.println("Division: " + quotient);
        System.out.println("Division: " + modulus);
        System.out.println("increment: " + num1);
        System.out.println("decrement " + num2);

    }
}
