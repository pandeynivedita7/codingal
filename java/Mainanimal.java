// This activity is mainly to explain multilevel inheritance

// Parent class
class Animal {
    void eat() {
        System.out.println("eating...Animal class...eat method");
    }
}

// First-level child class
class Lion extends Animal {
    void roar() {
        System.out.println("Roar...Lion class...roar method");
    }
}

// Second-level child class (child of Lion)
class BabyLion extends Lion {
    void weep() {
        System.out.println("weeping...BabyLion class...weep method");
    }
}

// Main class containing the entry point of the program
public class Mainanimal {
    public static void main(String[] args) {
        BabyLion obj = new BabyLion(); // Creating object of most derived class
        obj.weep(); // Method of BabyLion
        obj.roar(); // Inherited from Lion
        obj.eat(); // Inherited from Animal
    }
}
