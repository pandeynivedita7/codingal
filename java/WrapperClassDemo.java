public class WrapperClassDemo {
    public static void main(String[] args) {
        // 1. AUTOBOXING - Primitive to Wrapper (automatic)
        Integer num1 = 10; // int to Integer JVM automatically converts
        Double num2 = 5.5; // double to Double
        Character ch = 'A'; // char to Character
        Boolean flag = true; // boolean to Boolean

        System.out.println("=== AUTOBOXING ===");
        System.out.println("Integer: " + num1);
        System.out.println("Double: " + num2);
        System.out.println("Character: " + ch);
        System.out.println("Boolean: " + flag);

        // 2. UNBOXING - Wrapper to Primitive (automatic)
        int primitiveInt = num1; // Integer to int
        double primitiveDouble = num2; // Double to double

        System.out.println("\n=== UNBOXING ===");
        System.out.println("Primitive int: " + primitiveInt);
        System.out.println("Primitive double: " + primitiveDouble);

        // 3. EXPLICIT CONVERSION using valueOf()
        Integer num3 = Integer.valueOf(100);// create object of Integer class
        Double num4 = Double.valueOf(99.99);// create object of Double class

        System.out.println("\n=== EXPLICIT CONVERSION ===");
        System.out.println("valueOf(100): " + num3);
        System.out.println("valueOf(99.99): " + num4);

        // 4. STRING TO WRAPPER/PRIMITIVE
        String str1 = "123";// string to be converted to number
        String str2 = "45.67";// string to be converted to double JVM automatically converts
        // string methods to convert 1 datatype to another
        Integer converted1 = Integer.parseInt(str1); // String to int
        Double converted2 = Double.parseDouble(str2); // String to double
        Integer converted3 = Integer.valueOf(str1); // String to Integer

        System.out.println("\n=== STRING CONVERSION ===");
        System.out.println("parseInt(\"123\"): " + converted1);
        System.out.println("parseDouble(\"45.67\"): " + converted2);
        System.out.println("valueOf(\"123\"): " + converted3);

        // 5. WRAPPER TO STRING
        Integer num5 = 500;
        String str3 = num5.toString();
        String str4 = Integer.toString(600);// str4="600"

        System.out.println("\n=== WRAPPER TO STRING ===");
        System.out.println("Using toString(): " + str3);
        System.out.println("Using Integer.toString(): " + str4);

        // 6. USEFUL WRAPPER CLASS METHODS
        System.out.println("\n=== USEFUL METHODS ===");
        System.out.println("MAX_VALUE of Integer: " + Integer.MAX_VALUE);
        System.out.println("MIN_VALUE of Integer: " + Integer.MIN_VALUE);
        System.out.println("Compare 10 and 20: " + Integer.compare(10, 20));
        System.out.println("Is 'A' a digit? " + Character.isDigit('A'));// false
        System.out.println("Is '5' a digit? " + Character.isDigit('5'));// true
        System.out.println("Uppercase of 'a': " + Character.toUpperCase('a'));

        // 7. COMPARISON
        Integer a = 100;
        Integer b = 100;
        Integer c = 200;

        System.out.println("\n=== COMPARISON ===");
        System.out.println("a.equals(b): " + a.equals(b));// True
        System.out.println("a.equals(c): " + a.equals(c)); // False
        System.out.println("a == b: " + (a == b)); // True for -128 to 127 (cached)
        System.out.println("a.compareTo(c): " + a.compareTo(c)); // -1 (a < c)

        // 8. NULL VALUES (advantage of wrapper classes)
        Integer nullableInt = null; // Can be null
        // int primitiveInt2 = null; // ERROR - primitives cannot be null
        // size of interger is 4 bytes -127 to +127
        System.out.println("\n=== NULL HANDLING ===");
        System.out.println("Nullable Integer: " + nullableInt);

    }
}
