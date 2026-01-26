import java.util.Scanner;

public class GetToOne {
    public static void main(String[] args) {
        // Ask the user for the number they want to check.
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the number you want to check.");
        int myNum = input.nextInt();

        // Print the results by calling getToOne
        System.out.println("The number of divisions by 2 to get " + myNum + " down to one is " + divideToOne(myNum));

    }

    static int divideToOne(int num) {
        // count will hold the value of how many divisions we've done
        int count = 0;

        // while num is greater than 1, continue to divide by 2 and print the results
        // each time
        while (num > 1) {
            num = num / 2;
            System.out.println(num);
            count++;
        }
        return count;
    }
}