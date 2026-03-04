import java.util.Scanner;

public class SumToProgram1 {

    // Returns the smallest i such that 1 + 2 + ... + i > num
    static int sumTo(int num) {
        int i = 1;
        int sum = 0;

        while (true) {
            sum += i;// 1+2=3+3=6 6+4=10
            if (sum > num) {// 10>7
                return i;
            }
            i++;// 5
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);// 7

        System.out.print("Enter a number: ");
        int num = sc.nextInt();

        int result = sumTo(num);
        System.out.println("Smallest i such that sum(1..i) > " + num + " is: " + result);

        sc.close();
    }
}
