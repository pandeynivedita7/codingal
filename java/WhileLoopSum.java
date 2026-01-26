import java.util.Scanner;

public class WhileLoopSum {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");// 10
        int n = sc.nextInt();

        int sum = 0;// result variable
        int i = 1;// starting point 5

        // while loop to calculate sum
        while (i <= n) {// 1<=10 true
            sum = sum + i;// sum=0+1=1, sum=1+2=3, sum=3+3=6
            i++;
        }

        System.out.println("Sum of numbers from 1 to " + n + " is: " + sum);
    }
}
