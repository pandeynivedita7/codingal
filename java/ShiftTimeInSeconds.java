public class ShiftTimeInSeconds {
    public static void main(String[] args) {

        int hours = 12;
        int minutes = 14;
        int seconds = 16;

        int totalSeconds = 0;

        // Convert hours to seconds using a compound operator
        totalSeconds += hours * 3600; // += used here tottalSeconds=totalSecounds+hours*360

        // Convert minutes to seconds
        totalSeconds += minutes * 60;

        // Add remaining seconds
        totalSeconds += seconds;

        System.out.println("Total shift time in seconds: " + totalSeconds);
    }
}
