public class TextMessage {

    // Instance variables
    private String sender;
    private String receiver;
    private String message;
    private String timeStamp;

    // Constructor
    public TextMessage(String s, String r, String m, String t) {
        sender = s;
        receiver = r;
        message = m;
        timeStamp = t;
    }

    // toString method
    public String toString() {
        return "From: " + sender +
                "\nTo: " + receiver +
                "\nMessage: " + message +
                "\nTime: " + timeStamp;
    }

    // Accessor methods
    public String getSender() {
        return sender;
    }

    public String getReceiver() {
        return receiver;
    }

    public String getMessage() {
        return message;
    }

    public String getTimeStamp() {
        return timeStamp;
    }

    // Main method
    public static void main(String[] args) {

        // Creating object
        TextMessage msg1 = new TextMessage(
                "Nivedita",
                "Pandey",
                "Hello Bob!",
                "10:30 AM");

        // Printing using toString
        System.out.println(msg1);

        // Accessing values using getter methods
        System.out.println("\nAccessing individually:");
        System.out.println("Sender: " + msg1.getSender());
        System.out.println("Receiver: " + msg1.getReceiver());
        System.out.println("Message: " + msg1.getMessage());
        System.out.println("Time: " + msg1.getTimeStamp());
    }
}