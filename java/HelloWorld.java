// Week 1 - Introduction to Java
// This program demonstrates basic Java syntax, print statements, and commenting.

public class HelloWorld {
    public static void main(String[] args) {

        // Single-line comment: prints a simple message
        System.out.println("Hello, World!");

        // Printing multiple messages
        System.out.println("Welcome to Java Programming!");
        System.out.println("Let's learn how to write clean code.");

        /*
         * Multi-line comment:
         * You can also print text on the same line using print() instead of println().
         */
        System.out.print("Hello ");
        System.out.print("again, using print() method.\n"); // \n moves to the next line

        // Combining text and variables
        String name = "Student";
        String address = "India";
        System.out.println("Hello, " + name + "! Let's start coding.");
        System.out.println(address);
        System.out.println("Address," + address + " thius is my address");
    }
}
