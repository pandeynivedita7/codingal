class ShapeArea {

    // Area of rectangle
    int area(int length, int width) {
        return length * width;
    }

    // Area of square (method overloading)
    int area(int side) {
        return side * side;
    }

    public static void main(String[] args) {
        ShapeArea obj = new ShapeArea();
        // multiple methods with the same name but different parameter lists.
        System.out.println("Area of Rectangle: " + obj.area(10, 5));
        System.out.println("Area of Square: " + obj.area(4));
    }
}
// key points same method name different parameters/same parameter complier time
// decides which method to call