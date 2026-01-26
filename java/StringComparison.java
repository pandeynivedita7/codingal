public class StringComparison {
    public static void main(String[] args) {

        String first = "HelloWorld";
        String second = "Hello";
        String third = "World";

        // Concatenate second and third strings
        String combined = second + third;

        // Compare first string with combined string
        if (first.equals(combined)) {
            System.out.println("First string IS equal to second and third combined.");
        } else {
            System.out.println("First string is NOT equal to second and third combined.");
        }
    }
}
// Then, print out whether or not the first string is equal to the second and
// third string concatenated together. Don’t worry about spaces at the beginning
// or end of strings unless you want to!