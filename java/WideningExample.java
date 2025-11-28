public class WideningExample {
    public static void main(String[] args) {
        int num = 10; // int
        double result = num; // int → double (automatic)

        System.out.println("Int value: " + num);
        System.out.println("After Widening to double: " + result);
    }
}
/*
 * Widening (Implicit) Type Casting
 * 
 * Smaller data type → Larger data type
 * 
 * Java does this automatically.
 * 
 * No data loss.
 */