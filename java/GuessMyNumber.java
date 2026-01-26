import java.util.Scanner;

public class GuessMyNumber {

    public static void guessMyNumber(int secretNumber) {
        Scanner sc = new Scanner(System.in);
        int guess = 0;

        while (guess != secretNumber) {
            System.out.print("Enter your guess: ");
            guess = sc.nextInt();

            if (guess < secretNumber) {
                System.out.println("Too low! Try again.");
            } else if (guess > secretNumber) {
                System.out.println("Too high! Try again.");
            }
        }

        System.out.println("Correct! You guessed the secret number.");
        sc.close();
    }

    public static void main(String[] args) {
        int secretNumber = 16; // secret number between 1 and 100
        guessMyNumber(secretNumber);
    }
}
