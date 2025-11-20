public class MaxValue {
    public static void main(String[] args) {
        int[] scores = { 12, 45, 7, 89, 23 };
        int max = scores[0];

        for (int i = 1; i < scores.length; i++) {
            if (scores[i] > max) {
                max = scores[i];
            }
        }

        System.out.println("Maximum = " + max);
    }
}
