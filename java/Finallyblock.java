public class Finallyblock {
    public static void main(String[] args) {
        try {
            int a = 50 / 0;
        } catch (ArithmeticException e) {
            System.out.println("Error occurred");
        } finally {
            System.out.println("This will always run");
        }
    }
}
