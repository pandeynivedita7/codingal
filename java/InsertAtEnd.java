public class InsertAtEnd {
    public static void main(String[] args) {
        int[] arr = new int[5];
        int size = 0;

        arr[size] = 11;
        size++;

        arr[size] = 22;
        size++;

        arr[size] = 33;
        size++;

        for (int i = 0; i < size; i++) {
            System.out.println(arr[i]);
        }
    }
}
