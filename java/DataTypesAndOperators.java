public class DataTypesAndOperators {
    public static void main(String[] args) {

        // Primitive data types
        int age = 25;
        double salary = 45678.50;
        char grade = 'A';
        boolean isEmployee = true;

        // Print data types
        System.out.println("Age: " + age); // Integer
        System.out.println("Salary: " + salary); // Double
        System.out.println("Grade: " + grade); // Character
        System.out.println("Is Employee: " + isEmployee); // Boolean

        // Operators
        int a = 10;
        int b = 3;

        // Arithmetic Operators
        System.out.println("Addition: " + (a + b));
        System.out.println("Subtraction: " + (a - b));
        System.out.println("Multiplication: " + (a * b));
        System.out.println("Division: " + (a / b));
        System.out.println("Modulus: " + (a % b));

        // Relational Operators
        System.out.println("a > b: " + (a > b));
        System.out.println("a == b: " + (a == b));

        // Logical Operator
        System.out.println("(a > 5) && (b < 5): " + ((a > 5) && (b < 5)));
    }
}
