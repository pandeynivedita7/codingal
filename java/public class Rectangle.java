public class Rectangle {
    private int width;
    private int height;

    /**
     * This is the constructor to create a Rectangle.
     * To create a Rectangle we need to know its width
     * and height.
     */
    public Rectangle(int rectWidth, int rectHeight) {
        width = rectWidth;
        height = rectHeight;
    }

    /**
     * This method computes and prints the
     * area of the Rectangle.
     * Note it will print the area of the
     * Rectangle object that called it using
     * the dot operator!
     */
    public void printArea() {
        int area = width * height;
        System.out.println(area);
    }

    /**
     * This is the toString method. It returns a String
     * representation of the object.
     */
    public String toString() {
        return "Rectangle with width: " + width + " and height: " + height;
    }
}

public class RectangleTester {
    public static void main(String[] args) {
        /*
         * Rectangle is the name of the class. Every Rectangle
         * has a width and a height. But the specific instances
         * have their own dimensions.
         */
        Rectangle r1 = new Rectangle(10, 2);
        System.out.println(r1);

        System.out.print("Area of r1: ");
        r1.printArea();

        // Rectangle is the class and also the type of this object.
        Rectangle r2 = new Rectangle(5, 15);
        System.out.println(r2);

        System.out.print("Area of r2: ");
        r2.printArea();

    }
}