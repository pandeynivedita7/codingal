public class DivisionExample {

    static int divide(int a, int b) {
        // Precondition: b != 0
        return a / b;
    }

    public static void main(String[] args) {
        System.out.println(divide(10, 2)); // Valid
        // System.out.println(divide(10, 0)); // Invalid: breaks precondition
    }
}