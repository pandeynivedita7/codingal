// Define interface
interface Animal {
    void eat(); // abstract method

    void sleep(); // abstract method
}

// Implement interface
class Dog implements Animal {
    public void eat() {
        System.out.println("Dog eats bones");
    }

    public void sleep() {
        System.out.println("Dog sleeps in a kennel");
    }
}

public class MainInterface {
    public static void main(String[] args) {
        Dog d = new Dog();
        d.eat();
        d.sleep();
    }
}
