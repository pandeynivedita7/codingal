public class ReverseArray {
    public static void main(String[] args) {
        int[] arr = { 3, 6, 9, 12, 15 };

        for (int i = arr.length - 1; i >= 0; i--) {
            System.out.print(arr[i] + " ");
        }
    }
}
