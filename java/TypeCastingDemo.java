public class TypeCastingDemo {
    public static void main(String[] args) {

        // Widening
        int a = 20;
        double b = a; // implicit automatic 20.0
        System.out.println("Widening int to double: " + b);

        // Narrowing expliicity Manual conversion done by the programmer when converting
        // a larger data type to a smaller one. possible data loss
        double x = 9.99;
        int y = (int) x; // explicit 9
        System.out.println("Narrowing double to int: " + y);
    }
}
// converting a datatype to another
// implicit(widening) and explicit(narrowing) type casting
// Automatic conversion done by Java when converting a smaller data type to a
// implicitly
// larger data type. no data loss safe conversion
// byte -> short -> char -> int -> long -> float -> double datatype gtreater
// than