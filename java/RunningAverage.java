import java.util.Scanner;

public class RunningAverage {
    public static void main(String[] args) {

        int numInputs = 0;
        double totalTime = 0;

        average(numInputs, totalTime);
    }

    public static void average(int myNumInputs, double myTotalTime) {

        final double SENTINEL = -1;
        Scanner input = new Scanner(System.in);

        while (true) {
            System.out.print("Input your 40 yard dash time in seconds (-1 to stop): ");
            double time = input.nextDouble();

            if (time == SENTINEL) { // stop condition
                break;
            }

            myNumInputs++;
            myTotalTime += time;
        }

        if (myNumInputs == 0) {
            System.out.println("No times entered. Average cannot be calculated.");
        } else {
            double average = myTotalTime / myNumInputs;
            System.out.println("Average 40 yard dash time: " + average + " seconds.");
        }

        input.close();
    }
}
