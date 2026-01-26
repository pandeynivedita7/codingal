public class LogicalOperatorsExample {
    public static void main(String[] args) {

        int a = 10;
        int b = 5;

        // if with logical AND (&&)
        if (a > 5 && b > 3) {// both conditions must be true to execute this block
            System.out.println("Both conditions are true");
        }

        // else if with logical OR (||)
        else if (a > 5 || b > 10) {// at least one condition must be true to execute this block
            System.out.println("At least one condition is true");
        }

        // if with logical NOT (!)
        if (!(a < b)) {
            System.out.println("a is not less than b");
        }
    }
}
