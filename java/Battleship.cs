public class Battleship {

    // Instance variable to store the position of the ship
    int position;

    // Constructor to initialize the position
    public Battleship(int startPosition) {
        position = startPosition;
    }

    // move method as described
    public void move(boolean safeToMoveForward) {
        if (safeToMoveForward) {
            position += 7;
        } else {
            position -= 2;
        }
    }

    // Getter method to check the current position
    public int getPosition() {
        return position;
    }

    // Main method for testing
    public static void main(String[] args) {
        Battleship ship = new Battleship(0);

        ship.move(true);   // safe to move forward
        System.out.println("Position after safe move: " + ship.getPosition());

        ship.move(false);  // not safe to move forward
        System.out.println("Position after unsafe move: " + ship.getPosition());
    }
}
