public class Square {
    private int side;

    // Constructor
    public Square(int s) {
        side = s; // no 'this' used
    }

    // Method to calculate area
    public int getArea() {
        return side * side;
    }

    // Getter for side
    public int getSide() {
        return side;
    }

    // toString method
    public String toString() {
        return "Square: " + side;
    }
}

// Tester Class
class SquareTester {
    public static void main(String[] args) {
        Square s1 = new Square(10);
        System.out.println(s1);
        System.out.println(s1.getArea());
    }
}
