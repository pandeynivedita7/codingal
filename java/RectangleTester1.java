public class RectangleTester
{
    // RectangleOne class inside same file
    static class RectangleOne
    {
        private int width;
        private int height;

        // Constructor
        public RectangleOne(int rectWidth, int rectHeight)
        {
            width = rectWidth;
            height = rectHeight;
        }

        // Returns the area of the rectangle
        public int getArea()
        {
            return width * height;
        }

        // Returns true if the rectangle is a square
        public boolean isSquare()
        {
            if(width == height)
                return true;
            return false;
        }

        // Sets width ONLY IF newWidth is positive
        // Returns true if width was updated
        public boolean setWidth(int newWidth)
        {
            if(newWidth > 0)
            {
                width = newWidth;
                return true;
            }
            return false;
        }

        // Sets height ONLY IF newHeight is positive
        // Returns true if height was updated
        public boolean setHeight(int newHeight)
        {
            if(newHeight > 0)
            {
                height = newHeight;
                return true;
            }
            return false;
        }

        // Returns a String representation of the object
        public String toString()
        {
            return "Rectangle with width: " + width + " and height: " + height;
        }
    }

    // Main method
    public static void main(String[] args)
    {
        // Create Rectangle objects
        RectangleOne lunchBox = new RectangleOne(8, 8);
        RectangleOne pencilBox = new RectangleOne(3, 10);

        System.out.println("lunchBox: " + lunchBox);
        System.out.println("pencilBox: " + pencilBox);

        // Check if they're squares
        System.out.println("\nLunchbox is square: " + lunchBox.isSquare());
        System.out.println("PencilBox is square: " + pencilBox.isSquare());

        // Try to set width to negative number
        if(pencilBox.setWidth(-10))
        {
            System.out.println("Successfully updated width");
        }
        else
        {
            System.out.println("Width update failed (must be positive)");
        }

        // Set height
        if(pencilBox.setHeight(4))
        {
            System.out.println("Successfully updated height");
        }

        // Print out final state of objects
        System.out.println("\nlunchBox: " + lunchBox);
        System.out.println("pencilBox: " + pencilBox);
    }
}
