class Animal {
    void sound() {
        System.out.println("Animal makes a sound");
    }
}

class Dog extends Animal {
    @Override // optional complier more readable
    void sound() {
        System.out.println("Dog barks");
    }
}

public class MainSound {
    public static void main(String[] args) {
        Animal a = new Dog(); // Upcasting
        a.sound(); // Output: Dog barks (not Animal makes a sound)
    }
}
