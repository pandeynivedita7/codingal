public class Rectangle {

    private int width;
    private int height;

    // Constructor
    public Rectangle(int width, int height) {
        this.width = width;
        this.height = height;
    }

    // Method to calculate area
    public int getArea() {
        return this.width * this.height;
    }

    // Getter for height
    public int getHeight() {
        return height;
    }

    // Getter for width
    public int getWidth() {
        return width;
    }

    // toString method
    public String toString() {
        return "Rectangle with width: " + width + " and height: " + height;
    }

    // Main method (Tester inside same file)
    public static void main(String[] args) {

        Rectangle r1 = new Rectangle(10, 2);
        System.out.println(r1);
        System.out.println("Area of r1: " + r1.getArea());

        Rectangle r2 = new Rectangle(5, 15);
        System.out.println(r2);
        System.out.println("Area of r2: " + r2.getArea());
    }
}