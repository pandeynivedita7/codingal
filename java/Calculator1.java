class Calculator1 {

    // Add two integers
    int add(int a, int b) {
        return a + b;
    }

    // Add three integers (overloading)
    int add(int a, int b, int c) {
        return a + b + c;
    }

    // Add two decimal numbers (overloading)
    double add(double a, double b) {
        return a + b;
    }

    public static void main(String[] args) {
        Calculator1 calc = new Calculator();

        System.out.println(calc.add(10, 20)); // 2 integers
        System.out.println(calc.add(5, 10, 15)); // 3 integers
        System.out.println(calc.add(2.5, 3.5)); // 2 doubles
    }
}
