class Student {
    private String firstName;
    private String lastName;
    private int gradeLevel;
    private double gpa;

    // Constructor with GPA
    public Student(String firstName, String lastName, int gradeLevel, double gpa) {
        this.firstName = firstName;
        // studentname=firstName;
        this.lastName = lastName;
        this.gradeLevel = gradeLevel;
        this.gpa = gpa;
    }

    // Constructor without GPA (default 0.0)
    public Student(String firstName, String lastName, int gradeLevel) {
        this(firstName, lastName, gradeLevel, 0.0);
    }

    // Setter methods
    public void setGPA(double gpa) {
        this.gpa = gpa;
    }

    public void setGradeLevel(int gradeLevel) {
        this.gradeLevel = gradeLevel;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    // Getter methods
    public String getFirstName() {
        return firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public int getGradeLevel() {
        return gradeLevel;
    }

    public double getGPA() {
        return gpa;
    }

    // toString method
    public String toString() {
        return firstName + " " + lastName + " is in grade: " + gradeLevel;
    }
}

public class StudentTester {
    public static void main(String[] args) {
        Student alan = new Student("Alan", "Turing", 11);
        System.out.println("Default GPA: " + alan.getGPA());
        alan.setGPA(3.5);
        System.out.println("Updated GPA: " + alan.getGPA());
        alan.setGradeLevel(12);

        System.out.println(alan.getFirstName());
        System.out.println(alan.getGradeLevel());

        Student ada = new Student("Ada", "Livelace", 12, 4.0);

        System.out.print(ada.getFirstName() + " ");
        System.out.println(ada.getLastName());
        System.out.println("GPA: " + ada.getGPA());
        ada.setLastName("Lovelace");

        System.out.println(alan);
        System.out.println(ada);
    }
}
