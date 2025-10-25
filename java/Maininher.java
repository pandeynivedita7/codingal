class Mammals {
    void mam() {
        System.out.println("Inside Mammals Class");
    }
}

// First child class of Mammals
class Lion extends Mammals {
    void roar() {
        System.out.println("Inside Lion class");
    }
}

// Second child class of Mammals
class Human extends Mammals {
    void hum() {
        System.out.println("Inside Human class");
    }
}

public class Maininher {
    public static void main(String[] args) {
        // Create object of Lion
        Lion lionObj = new Lion();
        lionObj.roar(); // ✅ OK
        lionObj.mam(); // ✅ OK
        // lionObj.hum(); ❌ Not allowed

        // Create object of Human
        Human humanObj = new Human();
        humanObj.hum(); // ✅ OK
        humanObj.mam(); // ✅ OK
        // humanObj.roar(); ❌ Not allowed
    }
}
