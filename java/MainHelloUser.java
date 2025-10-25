import java.util.*;

class MainHelloUser {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);// user input Scanner objname=new Scanner() new word creating object
        // system in out in to take input out is used to display output
        System.out.println("Hello User please Enter your Name: ");
        String name = sc.nextLine();

        System.out.println("Enter your lucky number");
        int lucky = sc.nextInt();

        System.out.println(
                "Hello " + name + ", Your lucky number " + lucky + " shows you are really hardworking. Keep it up!");
    }
}
