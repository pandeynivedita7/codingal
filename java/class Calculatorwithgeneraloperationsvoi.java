class Calculatorwithgeneraloperationsvoidmethods {

    void add(int a, int b) {
        System.out.println("Addition = " + (a + b));
    }

    void sub(int a, int b) {
        System.out.println("Subtraction = " + (a - b));
    }

    void mul(int a, int b) {
        System.out.println("Multiplication = " + (a * b));
    }

    void div(int a, int b) {
        System.out.println("Division = " + (a / b));
    }
}

public class Main {
    public static void main(String[] args) {

        Calculatorwithgeneraloperationsvoidmethods c = new Calculatorwithgeneraloperationsvoidmethods();   // object

        int a = 10;
        int b = 5;

        c.add(a, b);
        c.sub(a, b);
        c.mul(a, b);
        c.div(a, b);
    }
}
