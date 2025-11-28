public class Calculatorvoidwithparameters {

    // void method with two int parameters
    void addNumbers(int a, int b) {
        int sum = a + b;
        System.out.println("Sum = " + sum);
    }

    public static void main(String[] args) {
        Calculatorvoidwithparameters calcu = new Calculatorvoidwithparameters();
        calcu.addNumbers(10, 20); // call method

    }
}
