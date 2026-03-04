public class Studentforeach {

    String firstName;
    String lastName;
    int grade;

    // Constructor
    Student(String f, String l, int g) {
        firstName = f;
        lastName = l;
        grade = g;
    }

    // Method to return first name
    public String getFirstName() {
        return firstName;
    }

    public static void main(String[] args) {

        Student julian = new Student("Julian", "Jones", 9);
        Student larisa = new Student("Larisa", "Torres", 10);
        Student amada = new Student("Amada", "Robin", 10);
        Student mikka = new Student("Mikka", "Leads", 9);
        Student jay = new Student("Jay", "Khalil", 10);

        Student[] classroom = {julian, larisa, amada, mikka, jay};

        // for-each loop
        for (Student student : classroom) {
            System.out.println(student.getFirstName());
        }
    }
}