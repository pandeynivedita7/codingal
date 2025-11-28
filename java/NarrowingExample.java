public class NarrowingExample {
    public static void main(String[] args) {
        double num = 10.75; // double
        int result = (int) num; // double → int (manual cast)

        System.out.println("Double value: " + num);
        System.out.println("After Narrowing to int: " + result);
    }
}
