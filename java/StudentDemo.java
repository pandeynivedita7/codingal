import java.util.Scanner;

// Class definition
class StudentDemo {
    // Instance variables
    String name;
    int age;
    double marks;

    // Method to take input from user
    void inputData() {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter student name: ");
        name = sc.nextLine();

        System.out.print("Enter student age: ");
        age = sc.nextInt();

        System.out.print("Enter student marks: ");
        marks = sc.nextDouble();
    }

    // Method to display data
    void displayData() {
        System.out.println("\n--- Student Details ---");
        System.out.println("Name  : " + name);
        System.out.println("Age   : " + age);
        System.out.println("Marks : " + marks);
    }
}

public class StudentDemo {
    public static void main(String[] args) {
        // Creating object
        Student s1 = new Student();

        // Calling methods
        s1.inputData();
        s1.displayData();
    }
}
