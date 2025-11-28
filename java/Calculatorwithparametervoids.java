class Calculatorwithparametervoids {

    // instance variables
    int a;
    int b;

    // constructor
    Calculator(int x, int y) {
        a = x;
        b = y;
    }

    // void methods with parameters
    void add(int x, int y) {
        System.out.println("Addition = " + (x + y));
    }

    void sub(int x, int y) {
        System.out.println("Subtraction = " + (x - y));
    }

    void mul(int x, int y) {
        System.out.println("Multiplication = " + (x * y));
    }

    void div(int x, int y) {
        System.out.println("Division = " + (x / y));
    }
}

public class Main {
    public static void main(String[] args) {

        // object created using constructor and instance variables
        Calculatorwithparametervoids c = new Calculatorwithparametervoids(10, 5);

        // calling void methods with parameters (using instance variables)
        c.add(a, b);
        c.sub(c.a, c.b);
        c.mul(c.a, c.b);
        c.div(c.a, c.b);
    }
}
