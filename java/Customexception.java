public class Customexception {// Throw your exception using throw.

    static void checkAge(int age) throws InvalidAgeException {
        if (age < 18) {
            throw new InvalidAgeException("Age must be 18 or above!");
        } else {
            System.out.println("Access Granted!");
        }
    }

    public static void main(String[] args) {
        try {
            checkAge(15); // testing
        } catch (InvalidAgeException e) {// e is simply a variable name
            System.out.println("Exception: " + e.getMessage());
        }
    }
}
// InvalidAgeException e = new InvalidAgeException("Age must be 18 or above!");
