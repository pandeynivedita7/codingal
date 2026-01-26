public class Robot {

    int distance = 0;

    // Moves the robot based on battery status
    public void move(boolean batteryFull) {
        if (batteryFull) {
            distance += 5; // move forward
        } else {
            distance -= 1; // move backward
        }
    }

    public static void main(String[] args) {
        Robot r = new Robot();

        r.move(true);
        System.out.println(r.distance);

        r.move(false);
        System.out.println(r.distance);
    }
}
