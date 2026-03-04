import java.util.Scanner;

public class passwordValidator {

    // Returns true if password is valid, otherwise false
    public static boolean passwordCheck(String password) {

        // Rule 1: at least 8 characters
        if (password.length() < 8) {
            return false;
        }

        // Allowed characters: letters + digits
        String letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String digits = "0123456789";

        // Rule 2: only letters and digits
        for (int i = 0; i < password.length(); i++) {
            String ch = password.substring(i, i + 1);

            if (letters.indexOf(ch) == -1 && digits.indexOf(ch) == -1) {// char not found -1 ch=a 0 ch @ -1 ch=0 0 ch&=-1
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String password = sc.nextLine();     // input password
        System.out.println(passwordCheck(password));  // print boolean result
    }
}
