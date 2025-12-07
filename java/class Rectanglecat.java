class Rectanglecat {
    public class Rectangle {// Attributes of the Rectangle class instance variable
        int width;
        int height;

        // Constructor to initialize width and height
        public Rectangle(int rectWidth, int rectHeight)// rectanglecat(int w,int h)
        {
            width = rectWidth;// width = w;
            height = rectHeight;// height = h;
        }

        int getArea() {
            return length * width;
        }

        int getPerimeter() {
            return 2 * (length + width);
        }

        String getInfo() {
            return "Rectangle Details:\n" +
                    "Length: " + length + " cm\n" +
                    "Width: " + width + " cm\n" +
                    "Area: " + getArea() + " sq.cm\n" +
                    "Perimeter: " + getPerimeter() + " cm";
        }
    }

    class Main {
    public static void main(String[] args) {
        Rectangle rect1 = new Rectangle(10, 5);
        Rectangle rect2 = new Rectangle(8, 6);
        
        System.out.println(rect1.getInfo());
        System.out.println("\n" + rect2.getInfo());
}