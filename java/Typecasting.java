public class Typecasting {
    public static void main(String[] args) {

        int a = 7;
        int b = 3;

        // Without typecasting (integer division)
        int avg1 = (a + b) / 2; // gives 5
        System.out.println("Average without typecast: " + avg1);

        // With typecasting (to get decimal value)
        double avg2 = (double) (a + b) / 2; // gives 5.0
        System.out.println("Average with typecast: " + avg2);

        // Another way
        double avg3 = ((a + b) / 2.0); // gives 5.0
        System.out.println("Average using 2.0: " + avg3);
    }
}
