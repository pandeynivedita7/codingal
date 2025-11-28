class Calculator123 {

    // instance variables
    int a;
    int b;

    // constructor to initialize instance variables
    Calculator123(int x, int y) {
        a = x;
        b = y;
    }

    // void methods
    void add() {
        System.out.println("Addition = " + (a + b));
    }

    void sub() {
        System.out.println("Subtraction = " + (a - b));
    }

    void mul() {
        System.out.println("Multiplication = " + (a * b));
    }

    void div() {
        System.out.println("Division = " + (a / b));
    }
}

public class Main {
    public static void main(String[] args) {

        // creating object and passing values to constructor
        Calculator123 c = new Calculator123(10, 5);
        Calculator123 c1 = new Calculator123(10,5);

        // calling methods
        c.add();
        c.sub();
        c1.mul();
        c1.div();
    }
}
