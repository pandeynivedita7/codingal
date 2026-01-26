import java.util.Scanner;

public class RPS {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter choice (rock / paper / scissors): ");
        String user = sc.next();

        String computer = "rock"; // fixed choice for simplicity

        if (user.equals(computer)) {
            System.out.println("Tie");
        } else if (user.equals("rock") && computer.equals("scissors")) {// logical conditions for user win add operator
                                                                        // do it will be true if both condtion are true
            System.out.println("You win");
        } else if (user.equals("paper") && computer.equals("rock")) {
            System.out.println("You win");
        } else if (user.equals("scissors") && computer.equals("paper")) {
            System.out.println("You win");
        } else {
            System.out.println("Computer wins");
        }

        sc.close();
    }
}
