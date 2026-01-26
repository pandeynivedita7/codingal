import java.util.Scanner;

public class VotingEligibility {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);// Creating Scanner object

        // Taking input from user
        System.out.print("Enter your age: ");
        int age = sc.nextInt();// Reading integer input

        // Checking eligibility
        if (age >= 18) {// True
            System.out.println("You are eligible to vote.");
        } else {//false
            System.out.println("You are NOT eligible to vote.");
        }

        sc.close();
    }
}
//nextInt() method is used to read an integer input from the user.
//next single word   //nextline() method is used to read a complete line of text input from the user.close() method is used to close the scanner object and free up resources.
