public class InsertInArray {
    public static void main(String[] args) {
        int[] arr = new int[6]; // one extra space for new element
        arr[0] = 3;
        arr[1] = 7;
        arr[2] = 9;
        arr[3] = 12;
        int size = 4; // current number of elements

        int position = 2; // index where we insert
        int value = 15;

        // Shift right
        for (int i = size; i > position; i--) {
            arr[i] = arr[i - 1];
        }

        // Insert value
        arr[position] = value;
        size++;

        // Print result
        for (int i = 0; i < size; i++) {
            System.out.println(arr[i]);
        }
    }
}
