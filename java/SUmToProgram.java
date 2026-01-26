import java.util.Scanner;

public class SumToProgram {

    // Returns the smallest i such that 1 + 2 + ... + i > num
    static int sumTo(int num) {//10
        int i = 1;
        int sum = 0;

        while (true) {
            sum += i;//7+5=12
            if (sum > num) {//12>10
                return i;//5
            }
            i++;//5
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int num = sc.nextInt();

        int result = sumTo(num);
        System.out.println("Smallest i such that sum(1..i) > " + num + " is: " + result);

        sc.close();
    }
}
