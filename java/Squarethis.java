public class Square {

    private int side;

    // Constructor
    public Square(int side) {
        this.side = side;
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
        return "Square with side: " + side;
    }

    // Main method (Tester inside same file)
    public static void main(String[] args) {

        Square s1 = new Square(4);
        System.out.println(s1);
        System.out.println("Area of s1: " + s1.getArea());

        Square s2 = new Square(7);
        System.out.println(s2);
        System.out.println("Area of s2: " + s2.getArea());
    }
}