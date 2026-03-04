class Studentwithoutthis {

    // Static variable (shared by all objects)
    static String schoolName = "ABC School";

    // Instance variable
    String studentName;

    // Constructor
    public Student(String name) {
        studentName = name;
    }

    // Static method
    public static void changeSchool(String newSchool) {
        schoolName = newSchool;
    }

    // Instance method
    public void display() {
        System.out.println("Name: " + studentName);
        System.out.println("School: " + schoolName);
    }
}

public class StaticDemo {

    public static void main(String[] args) {

        // Creating objects
        Student s1 = new Student("Riya");
        Student s2 = new Student("Aman");

        // Display initial values
        s1.display();
        System.out.println();
        s2.display();

        // Changing static variable using static method
        Student.changeSchool("XYZ Public School");

        System.out.println("\nAfter changing school name:\n");

        s1.display();
        System.out.println();
        s2.display();
    }
}