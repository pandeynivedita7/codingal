class Distance {

    private double feet;

    // Constructor
    public Distance(double startFeet) {
        feet = startFeet;
    }

    // Convert feet to yards
    public double toYards() {
        return feet / 3.0;
    }

    // Convert feet to inches
    public double toInches() {
        return feet * 12.0;
    }

    // Getter method
    public double getFeet() {
        return feet;
    }
}

public class DistanceTester {

    public static void main(String[] args) {

        // Creating Distance objects
        Distance gym = new Distance(213);
        Distance cafeteria = new Distance(128);
        Distance bestFriend = new Distance(10.5);

        // Printing required outputs
        System.out.println("Karel is " + gym.toYards() + " yards from the gymnasium.");
        System.out.println("Karel is " + cafeteria.getFeet() + " feet from the cafeteria.");
        System.out.println("Karel is " + bestFriend.toInches() + " inches from his best friend.");
    }
}