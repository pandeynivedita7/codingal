public class FractionSubtraction {
    public static void main(String[] args) {

        // Define values
        int a = 5;
        int b = 7;
        int c = 2;
        int d = 3;

        // Formula: (a/b) - (c/d) = (ad - bc) / (bd)
        int numerator = (a * d) - (b * c);
        int denominator = b * d;

        System.out.println("Result = " + numerator + "/" + denominator);
    }
}
