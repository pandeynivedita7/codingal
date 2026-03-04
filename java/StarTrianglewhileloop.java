public class StarTriangle {
    public static void main(String[] args) {
        int rows = 5;
        int i = 1;

        while (i <= rows) {//2<=5
            int j = 1;
            while (j <= i) {//2<=2
                System.out.print("*");//* */
                j++;//2
            }
            System.out.println();
            i++;//2
        }
    }
}
