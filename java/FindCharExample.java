public class FindCharExample {

    public static boolean findChar(String string, char key) {
        for (int index = 0; index < string.length(); index++) {
            if (string.charAt(index) == key) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        String text = "computer";
        char searchKey = 'p';

        boolean result = findChar(text, searchKey);

        System.out.println("Character found: " + result);
    }
}
