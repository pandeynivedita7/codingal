import java.util.Scanner;
import java.util.Random;

public class GuessTheNumber {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        // Generate random number between 1 and 100
        int secretNumber = random.nextInt(100) + 1;
        // int secretNumber = random.nextInt(1,100 + 1); // Java 17+ syntax
        int guess;
        int attempts = 0;

        System.out.println("Welcome to Guess the Number Game!");
        System.out.println("I have picked a number between 1 and 100.");
        System.out.println("Try to guess it!\n");

        // Game loop
        while (true) {// Infinite loop until the correct guess
            System.out.print("Enter your guess: ");
            guess = scanner.nextInt();
            attempts++;

            if (guess < secretNumber) {
                System.out.println("Too low! Try again.\n");
            } else if (guess > secretNumber) {
                System.out.println("Too high! Try again.\n");
            } else {
                System.out.println("\n🎉 Congratulations! You guessed it!");
                System.out.println("The number was: " + secretNumber);
                System.out.println("You took " + attempts + " attempts.");
                break;
            }
        }

        scanner.close();
    }
}```

**Example Output:**```
Welcome to
Guess the
Number Game!
I have
picked a
number between 1 and 100.
Try to
guess it!

Enter your guess:50
Too high!
Try again.

Enter your guess:25
Too low!
Try again.

Enter your guess:37
Too high!
Try again.

Enter your guess:31
Too low!
Try again.

Enter your guess:34
Too high!
Try again.

Enter your guess:32
Too low!
Try again.

Enter your guess:33

🎉Congratulations!
You guessed it!
The number was:33
You took 7 attempts
.