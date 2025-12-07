// try catch finally throw throws
/* try{
risky code
catch(Exception e)
{
what it should do f error comes
}
finally
{ always run this code no matter what
}} */
public class DividebyZero {
    public static void main(String[] args) {
        try {
            int a = 10;
            int b = 0;
            int result = a / b; // risky
            System.out.println("Result: " + result);

        } catch (ArithmeticException e) {
            System.out.println("Error: Cannot divide by zero!");
        }
    }
}
