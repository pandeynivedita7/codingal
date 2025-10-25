//scanner utlil
class Box {
    // Private variables
    private double length;
    private double breadth;
    private double height;

    // Setters
    public void setDimensions() {
        if (l > 0 && b > 0 && h > 0) {
            length = l;
            breadth = b;
            height = h;
        }
    }

    // Getter for volume
    public double getVolume() {
        return length * breadth * height;
    }
}

public class MainBox {
    public static void main(String[] args) {
        Box box = new Box();
        box.setDimensions(4, 3, 2); // setting dimensions
        System.out.println("Volume of Box: " + box.getVolume());
    }
}
