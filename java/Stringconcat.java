public class Stringconcat {
    public static void main(String[] args) {
        String str = "Java";
        str.concat(" Programming");
        // The original string remains unchanged because strings are immutable
        System.out.println(str); // Output: Java
    }
}
