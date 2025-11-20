public class CountEven {
    public static void main(String[] args) {
        int[] arr = { 2, 7, 8, 9, 10, 13 };
        int count = 0;

        for (int n : arr) {
            if (n % 2 == 0) {
                count++;
            }
        }

        System.out.println("Even count = " + count);
    }
}
