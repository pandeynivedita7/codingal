public class MathLibraryProgram {

    public static void main(String[] args) {

        int a = 16;
        int b = 5;

        System.out.println("Square Root of 16: " + Math.sqrt(a));// 4
        System.out.println("Power (2^5): " + Math.pow(2, b));
        System.out.println("Maximum: " + Math.max(a, b));// 16
        System.out.println("Minimum: " + Math.min(a, b));// 5
        System.out.println("Absolute Value of -10: " + Math.abs(-10));// 10
        System.out.println("Ceil of 4.3: " + Math.ceil(4.3));// 5
        System.out.println("Floor of 4.7: " + Math.floor(4.7));// 4
        System.out.println("Round of 4.5: " + Math.round(4.5));// 5
        System.out.println("Random Number: " + Math.random());// 0.0 to 1.0
    }
}
