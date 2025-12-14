public class MathOperationsDemo {
    public static void main(String[] args) {

        int a = 12, b = 4;

        System.out.println("Add: " + Math.addExact(a, b));
        System.out.println("Subtract: " + Math.subtractExact(a, b));
        System.out.println("Multiply: " + Math.multiplyExact(a, b));
        System.out.println("Divide: " + (a / b));
        System.out.println("Power: " + Math.pow(a, b));
        System.out.println("Square Root: " + Math.sqrt(a));
        System.out.println("Absolute: " + Math.abs(-25));
        System.out.println("Max: " + Math.max(a, b));
        System.out.println("Min: " + Math.min(a, b));
        System.out.println("Random: " + (int) Math.random() * 20); // generates a random number between 0 and 20 by
                                                                   // default 0 double value int type casting
        // math.random() generates a double value between 0.0 and 1.0
        // type casting to int will always result in 0 here
        

    }
}
/* fixed value random number */
