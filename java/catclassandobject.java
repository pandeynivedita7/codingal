class Cat {
    String name;
    int age;

    Cat() {
        name = "Unknown";
        age = 0;
    }

    Cat(String n, int a) {
        name = n;
        age = a;
    }

    void display() {
        System.out.println("Name: " + name + ", Age: " + age);
    }
}

public class catClassandobject {
    public static void main(String[] args) {

        Cat c1 = new Cat();
        c1.display();

        Cat c2 = new Cat("Kitty", 3);
        c2.display();
    }
}
