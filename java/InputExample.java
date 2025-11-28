import java.util.Scanner; //different Scanner methods to take input

public class InputExample {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        // Taking String input
        System.out.print("Enter your name: ");
        String name = input.nextLine(); // For String datatype variablename=scannervarname.methodmethod()

        // Taking int input
        System.out.print("Enter your age: ");
        int age = input.nextInt(); // For int

        // Taking double input
        System.out.print("Enter your marks: ");
        double marks = input.nextDouble(); // For double

        // Display output
        System.out.println("\n--- Output ---");
        System.out.println("Name  : " + name);
        System.out.println("Age   : " + age);
        System.out.println("Marks : " + marks);
    }
}
/*
 * Data Type Method Used Example
 * String nextLine() Reads a whole line (including spaces).
 * int nextInt() Reads an integer value.
 * double nextDouble() Reads a decimal (floating-point) value.
 */
