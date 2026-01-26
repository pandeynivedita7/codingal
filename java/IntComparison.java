public class IntComparison {
    public static void main(String[] args) {
        int a = 10;
        int b = 20;

        System.out.println(a == b); // false
        System.out.println(a != b); // true
        System.out.println(a > b); // false
        System.out.println(a < b); // true
        System.out.println(a >= b); // false
        System.out.println(a <= b); // true
    }
}

// string comparison .equals() method . compareTo() method
class StringComparison {
    public static void main(String[] args) {
        String str1 = "hello";
        String str2 = "world";
        String str3 = "Hello";

        // Using .equals() method
        System.out.println(str1.equals(str2)); // false
        System.out.println(str1.equals(str3)); // true

        // Using compareTo() method
        System.out.println(str1.compareTo(str2)); // negative value
        System.out.println(str2.compareTo(str1)); // positive value
        System.out.println(str1.compareTo(str3)); // 0
    }
}