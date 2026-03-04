public class AdditionTable {
    public static void main(String[] args) {

        int i = 0;

        while (i <= 10) {
            int j = 0;
            while (j <= 10) {
                System.out.print((i + j) + "\t");
                j++;
            }
            System.out.println();
            i++;
        }
    }
}
