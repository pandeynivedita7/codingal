public class Student {

    private String firstName;
    private String lastName;
    private int gradeLevel;
    private double gpa;

    // 4-parameter constructor
    public Student(String firstName, String lastName, int gradeLevel, double gpa) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.gradeLevel = gradeLevel;
        this.gpa = gpa;
    }

    // 3-parameter constructor (constructor overloading)
    public Student(String firstName, String lastName, int gradeLevel) {
        this(firstName, lastName, gradeLevel, 0.0);
    }

    // Setters
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

    // Getters
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
        return firstName + " " + lastName +
                " is in grade: " + gradeLevel +
                " with GPA: " + gpa;
    }

    // Main method for testing
    public static void main(String[] args) {

        Student s1 = new Student("Nivedita", "Pandey", 10, 9.1);
        System.out.println(s1);

        Student s2 = new Student("Rahul", "Sharma", 8);
        System.out.println(s2);

        s2.setGPA(8.5);
        System.out.println("Updated GPA of s2: " + s2.getGPA());
    }
}