public class sumwithforloop {
    public static void main(String[] args) {
        int min = 1;
        int max = 50;
        int sum = 0;
        for (int i = min; i <= max; i++) {
            sum += i;
        }
        System.out.println("The sum is: " + sum);
    }
}