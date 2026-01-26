class DefaultParameterExample {

    // Method with parameter
    void display(int x) {
        System.out.println("Value: " + x);
    }

    // Method without parameter (default value)
    void display() {
        display(10); // default value
    }

    public static void main(String[] args) {
        DefaultParameterExample obj = new DefaultParameterExample();

        obj.display();      // uses default value
        obj.display(25);    // uses given value
    }
}
