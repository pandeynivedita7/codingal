public class TicketTester {
    public static void main(String[] args) {
        double basePrice = 300;

        // Movie tickets for a group
        MovieTicket ticket = new MovieTicket(basePrice, 6);
        System.out.println("Movie Night");
        System.out.println(ticket);

        // Apply discount
        ticket.applyDiscount();
        System.out.println("\nAfter Discount");
        System.out.println(ticket);

        // Fewer people
        System.out.println("\n\n");
        ticket = new MovieTicket(basePrice, 3);
        System.out.println("Movie Night");
        System.out.println(ticket);

        ticket.applyDiscount();
        System.out.println("\nAfter Discount");
        System.out.println(ticket);

        // Single person
        System.out.println("\n\n");
        ticket = new MovieTicket(basePrice, 1);
        System.out.println("Movie Night");
        System.out.println(ticket);

        ticket.applyDiscount();
        System.out.println("\nAfter Discount");
        System.out.println(ticket);
    }
}

public class MovieTicket {
    private double price;
    private int people;

    public MovieTicket(double p, int n) {
        price = p;
        people = n;
    }

    // Discount depends on number of people
    public void applyDiscount() {
        if (people >= 5)
            price -= 50;
        else if (people >= 3)
            price -= 30;
        else
            price -= 10;
    }

    public String toString() {
        return "People: " + people + "\nTotal Price: " + price;
    }
}
