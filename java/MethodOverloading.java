class Calculator1 {

    // Method with two int parameters
    int add(int a, int b) {
        return a + b;
    } // method name same, parameter list different

    // Method with three int parameters
    int add(int a, int b, int c) {
        return a + b + c;
    }

    // Method with double parameters
    double add(double a, double b) {
        return a + b;
    }

    // main method (program entry point)
    public static void main(String[] args) {
        Calculator1 calc = new Calculator1();

        System.out.println("Addition of 2 ints: " + calc.add(10, 20));
        System.out.println("Addition of 3 ints: " + calc.add(10, 20, 30));
        System.out.println("Addition of 2 doubles: " + calc.add(10.5, 20.3));
    }
}
