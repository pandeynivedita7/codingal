public class Student { // blueprint for student object

    int rollNumber;     // instance variable
    String name;
    double marks;

    // Parameterized constructor initializing instance variables
    Student(int rNo, String sName, double sMarks) { // allocating , initializing memory
        rollNumber = rNo;     // setting values
        name = sName;
        marks = sMarks;
    }

    // Method to display student details
    void display() {
        System.out.println("Student Roll Number: " + rollNumber);
        System.out.println("Student Name: " + name);
        System.out.println("Student Marks: " + marks);
    }

    // Main method
    public static void main(String[] args) {

        // Creating Student objects using constructor
        Student s1 = new Student(1, "Amit", 89.5);
        Student s2 = new Student(2, "Neha", 93.0);

        // Displaying student details
        s1.display();
        System.out.println("--------------------");
        s2.display();
    }
}
