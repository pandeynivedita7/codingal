class Studentsetget {

    // private variables (cannot be accessed directly)
    private String name;
    private int age;

    // getter for name
    public String getName() {
        return name;
    }
//A getter (get) and setter (set) in Java are methods used to access and modify private class variables. They provide a way to read and update the values of private fields from outside the class while maintaining encapsulation.
    // setter for name
   
    // getter for age
    public int getAge() {
        return age;
    }

    }
public class Main {
    public static void main(String[] args) {
        Student s = new Student();

        s.setName("Nivedita");  // setting value
        s.setAge(22);

        System.out.println(s.getName()); // reading value
        System.out.println(s.getAge());
    }
}

