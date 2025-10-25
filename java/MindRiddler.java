class Main123 {
    public static void main(String[] args) {

        int a = 10;
        int b = 5;
        System.out.println("==============Guess the Answers==========");

        System.out.println("Uninary Operator" + (a++));
        System.out.println("Uninary Operator" + (++a));
        System.out.println("Binary Operator");
        System.out.println("1+2 " + 1 + 2);
        System.out.println("1+2 " + (1 + 2));
        System.out.println(1 + 2 + " =3");
        int increment = ++a * b++;
        System.out.println(increment);
        // uncomment the next lines to know the values
        // System.out.println("Current Value of a: " +a);
        // System.out.println("Current Value of b: " +b);
        System.out.println("Ternany Operator");
        int largestNumber = (a > b) ? a : b;
        System.out.println("Largest of 2 numbers: " + largestNumber);// operands means alpha operator means symbol
        // arithmetic assignment comparsion(relational)
        // 2 operands and 1 operator 1 operands uninary operator
        /*
         * Increment & Decrement Operators
         * Used to increase/decrease a variable's value.
         * 
         * Operator Description Example
         * ++ Increment x++ or ++x
         * -- Decrement x-- or --x
         * a=5
         * a=a++
         * b=6
         * b=b--
         * a++ post increment This means it returns the original value, then increases a
         * by 1.
         * ++a pre increment This means it first increases a by 1, then returns the new
         * value.
         */

    }
}