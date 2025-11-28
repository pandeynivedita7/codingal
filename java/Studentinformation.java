class Student {
    int age;
    String name;

    // Constructor must be inside the class
    Student()// constructor initialize the value{
        age = 18;
        name = "Nisheeth";
    }

    void Display() {
        System.out.println(age + " " + name);
    }
}

public class Studentinformation {
    public static void main(String[] args) {// object memory allocation
        Student s = new Student();// object   class name object name=new class() new keywords create a object 
        s.Display();// using object s calling method display
    }
}
