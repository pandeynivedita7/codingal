public class TicketTester {
    public static void main(String[] args) {
        double basePrice = 300;

        MovieTicket ticket = new MovieTicket(basePrice, 6);
        System.out.println("Movie Night");
        System.out.println(ticket);

        ticket.applyDiscount();
        System.out.println("\nAfter Discount");
        System.out.println(ticket);

        System.out.println("\n");

        ticket = new MovieTicket(basePrice, 2);
        System.out.println("Movie Night");
        System.out.println(ticket);

        ticket.applyDiscount();
        System.out.println("\nAfter Discount");
        System.out.println(ticket);
    }
}

/* Second class in the same file (NOT public) */
class MovieTicket {
    private double price;
    private int people;

    public MovieTicket(double p, int n) {
        price = p;
        people = n;
    }

    public void applyDiscount() {
        if (people >= 5)
            price = price - 50;
        else if (people >= 3)
            price = price - 30;
        else
            price = price - 10;
    }

    public String toString() {
        return "People: " + people + "\nTotal Price: " + price;
    }
}
