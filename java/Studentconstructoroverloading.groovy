class Studentconstructoroverloading {

    int id;
    String name;
    int age;

    // 1️⃣ Default constructor
    Studentconstructoroverloading() {
        id = 0;
        name = "Not Assigned";
        age = 0;
    }

    // 2️⃣ Constructor with two parameters
    Student(int i, String n) {
        id = i;
        name = n;
        age = 18; // default age
    }

    // 3️⃣ Constructor with three parameters
    Student(int i, String n, int a) {
        id = i;
        name = n;
        age = a;
    }

    // Method to display details
    void display() {
        System.out.println(id + " " + name + " " + age);
    }

    public static void main(String[] args) {

        Student s1 = new Studentconstructoroverloading();// Calls default constructor
        Student s2 = new Studentconstructoroverloading(101, "Rahul");// Calls constructor with two parameters
        Student s3 = new Studentconstructoroverloading(102, "Anita", 21);// Calls constructor with three parameters

        s1.display();
        s2.display();
        s3.display();
    }
}