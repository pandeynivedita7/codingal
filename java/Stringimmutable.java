public class Stringimmutable {
    public static void main(String[] args) {
        String s1 = "Hello";
        String s2 = s1; // s2 refers to the same object as s1

        s1 = s1 + " World"; // creates a NEW String object

        System.out.println(s1); // Hello World
        System.out.println(s2); // Hello
    }
}
