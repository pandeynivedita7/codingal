public class TypeCastingDemo {
    public static void main(String[] args) {

        // Widening
        int a = 20;
        double b = a; // implicit
        System.out.println("Widening int to double: " + b);

        // Narrowing
        double x = 9.99;
        int y = (int) x; // explicit 9
        System.out.println("Narrowing double to int: " + y);
    }
}
