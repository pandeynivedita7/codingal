import java.util.Scanner;

public class CircleCalc {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter radius of circle: ");
        double radius = sc.nextDouble();

        double circumference = 2 * Math.PI * radius; // Formula: 2πr
        double area = Math.PI * radius * radius; // Formula: πr²

        System.out.println("Circumference: " + circumference);
        System.out.println("Area: " + area);

        sc.close();
    }
}
