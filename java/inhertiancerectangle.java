public class Rectangle {
    private int width;
    private int height;

    // Constructor
    public Rectangle(int rectWidth, int rectHeight) {
        width = rectWidth;
        height = rectHeight;
    }

    // Method to calculate area
    public int getArea() {
        return width * height;
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
}

// Tester Class
class RectangleTester extends ConsoleProgram {
    public void run() {
        // Create first Rectangle
        Rectangle r1 = new Rectangle(10, 2);
        System.out.println(r1);

        // Access the height of r1
        System.out.println("r1 height: " + r1.getHeight());

        // Create second Rectangle
        Rectangle r2 = new Rectangle(5, 15);
        System.out.println(r2);

        // Access the width of r2
        System.out.println("r2 width: " + r2.getWidth());
    }
}
