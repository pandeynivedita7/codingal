interface Vehicle {
    void start();

    default void stop() {
        System.out.println("Vehicle stopped");
    }

    static void fuelType() {
        System.out.println("Fuel type: Petrol");
    }
}

class Car implements Vehicle {
    public void start() {
        System.out.println("Car started");
    }
}

public class Main {
    public static void main(String[] args) {
        Car c = new Car();
        c.start();
        c.stop();          // default method
        Vehicle.fuelType(); // static method
    }
}


interface Test {
    default int x = 10;  // ❌ Error! “modifier default not allowed here”
}
