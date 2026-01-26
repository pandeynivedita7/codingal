import java.util.Scanner;// import java.utli.*; scanner class object new

class ScannerDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter name: ");
        String name = sc.nextLine();// string input

        System.out.print("Enter age: ");
        int age = sc.nextInt();// integer input

        System.out.print("Enter salary: ");
        double salary = sc.nextDouble();// double input
        // we dont have method for boolean and char in scanner class
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Salary: " + salary);

        sc.close();// garabage collection free memory
    }
}
