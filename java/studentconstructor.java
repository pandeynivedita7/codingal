class Student1 {

    int rollNumber; // instance variables
    String name;

    // Default constructor (no parameters)
    Student() {
        rollNumber = 1;     // assigning default values
        name = "Nisheetha";
    }

    // Method to display details
    void display() {
        System.out.println("Roll Number: " + rollNumber);
        System.out.println("Name: " + name);
    }

    public static void main(String[] args) {

        // Creating object using default constructor
        Student s1 = new Student();

        // Displaying values set by default constructor
        s1.display();
    }
}
