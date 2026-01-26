class Rectangle {
    private int width;
    private int height;

    public Rectangle(int w, int h) {
        width = w;
        height = h;
    }

    public int area() {
        return width * height;
    }

    public boolean isSquare() {
        if (width == height) {
            return true;
        } else {
            return false;
        }
    }

    public String toString() {
        return "Rectangle[width=" + width + ", height=" + height + "]";
    }
}

public class RectangleTester {
    public static void main(String[] args) {
        Rectangle rect1 = new Rectangle(4, 5);
        Rectangle rect2 = new Rectangle(6, 6);

        System.out.println("Area of rect1: " + rect1.area());
        System.out.println("Is rect1 a square? " + rect1.isSquare());
        System.out.println(rect1.toString());

        System.out.println("Area of rect2: " + rect2.area());
        System.out.println("Is rect2 a square? " + rect2.isSquare());
        System.out.println(rect2.toString());
    }
}
