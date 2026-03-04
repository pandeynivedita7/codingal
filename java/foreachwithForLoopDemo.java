public class foreachwithForLoopDemo {
    public static void main(String[] args) {

        int[] numbers = { 10, 20, 30, 40 };

        // Using for loop
        System.out.println("Using for loop:");
        for (int i = 0; i < numbers.length; i++) {
            System.out.println(numbers[i]);
        }

        // Using for-each loop
        System.out.println("Using for-each loop:");
        for (int num : numbers) {
            System.out.println(num);
        }
    }
}