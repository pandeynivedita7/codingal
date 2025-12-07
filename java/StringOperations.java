public class StringOperations {
    public static void main(String[] args) {

        String s = "Hello";
        String t = "World";

        // length()
        System.out.println("Length of s: " + s.length());

        // charAt()
        System.out.println("Character at index 1 in s: " + s.charAt(1));

        // concat()
        String result = s.concat(" ").concat(t);
        System.out.println("Concatenation: " + result);

        // toUpperCase() and toLowerCase()
        System.out.println("Uppercase: " + result.toUpperCase());
        System.out.println("Lowercase: " + result.toLowerCase());

        // substring()
        System.out.println("Substring (0 to 4): " + result.substring(0, 4));

        // equals() and equalsIgnoreCase()
        String a = "Java";
        String b = "java";
        System.out.println("equals(): " + a.equals(b)); // false
        System.out.println("equalsIgnoreCase(): " + a.equalsIgnoreCase(b)); // true

        // replace()
        System.out.println("Replace 'o' with '0': " + result.replace("o", "0"));

        // trim()
        String x = "   spaced text   ";
        System.out.println("Trimmed: '" + x.trim() + "'");

        // split()
       
        // contains()
        System.out.println("result contains 'World'? " + result.contains("World"));
    }
}
