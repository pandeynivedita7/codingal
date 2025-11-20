public class CreateArray1 {
    public static void main(String[] args) {
        // Create an array of 5 integers
        int[] numbers = new int[5];

        // Assign values
        numbers[0] = 10;
        numbers[1] = 20;
        numbers[2] = 30;
        numbers[3] = 40;
        numbers[4] = 50;

        // Print array
        for (int i = 0; i < numbers.length; i++) {
            System.out.println(numbers[i]);
        }
    }
}
