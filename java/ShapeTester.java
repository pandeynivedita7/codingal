class Triangle {

    private int base;
    private int height;

    // Constructor
    public Triangle(int tBase, int tHeight) {
        base = tBase;
        height = tHeight;
    }

    // Getter for base
    public int getBase() {
        return base;
    }

    // Setter for base
    public void setBase(int tBase) {
        base = tBase;//a=10
    }

    // Getter for height
    public int getHeight() {
        return height;
    }

    // Setter for height
    public void setHeight(int tHeight) {
        height = tHeight;
    }

    // Method to calculate area
    public double area() {
        return 0.5 * base * height;
    }

    // toString method
    public String toString() {
        return "Triangle with base = " + base +
                ", height = " + height +
                ", area = " + area();
    }
}

public class ShapeTester {

    public static void main(String[] args) {

        Triangle tri1 = new Triangle(3, 5);
        System.out.println(tri1);

        Triangle tri2 = new Triangle(4, 10);
        System.out.println("Base of tri2: " + tri2.getBase());

        tri2.setBase(6);
        System.out.println("Updated Base of tri2: " + tri2.getBase());

        System.out.println("Area of tri2: " + tri2.area());
    }
}