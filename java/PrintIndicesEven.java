public class PrintIndicesEven {

    public static void printEvenIndices(int[] arr) {
        // loop through array
        for (int i = 0; i < arr.length; i++) {
            
            // check for odd index
            if (i % 2 != 0) {
                System.out.println(arr[i]);
            }
        }
    }

    public static void main(String[] args) {
        int[] numbers = {10, 20, 30, 40, 50, 60};

        printEvenIndices(numbers);
    }
}