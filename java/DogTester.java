// Dog class
class Dog {

    // Instance variables
    private String name;
    private int age;
    private String breed;

    // Constructor 1: name, age, breed
    public Dog(String n, int a, String b) {
        name = n;
        age = a;
        breed = b;
    }

    // Constructor 2: name, age (breed = "unknown")
    public Dog(String n, int a) {
        name = n;
        age = a;
        breed = "unknown";
    }

    // Method to display dog details
    public void printDog() {
        System.out.println("Dog Name: " + name +
                ", Age: " + age +
                ", Breed: " + breed);
    }
}

// DogTester class (main class)
public class DogTester {

    public static void main(String[] args) {

        // First Dog object (3 parameters)
        Dog dog1 = new Dog("Buddy", 4, "Labrador");

        // Second Dog object (2 parameters)
        Dog dog2 = new Dog("Rocky", 2);

        // Print both objects
        dog1.printDog();
        dog2.printDog();
    }
}
