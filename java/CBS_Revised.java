import java.util.Scanner;

public class CBS_Revised {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // Storage for up to 100 customers
        String[] customerNames = new String[100];
        double[] customerBalances = new double[100];
        int count = 0;

        while (true) {

            // Menu
            System.out.println("\n=== Codingal Banking Services ===");
            System.out.println("1. Register New Customer");
            System.out.println("2. Edit Customer Name");
            System.out.println("3. View Balance");
            System.out.println("4. Deposit / Withdraw");
            System.out.println("5. Account Summary");
            System.out.println("6. Exit System");
            System.out.print("Choose an option: ");

            int option = sc.nextInt();
            sc.nextLine();

            switch (option) {

                case 1:
                    System.out.println("\n--- Register New Customer ---");

                    System.out.print("Enter Name: ");
                    customerNames[count] = sc.nextLine();

                    double openingBalance;
                    do {
                        System.out.print("Enter Opening Balance (>=0): ");
                        openingBalance = sc.nextDouble();
                    } while (openingBalance < 0);

                    customerBalances[count] = openingBalance;

                    System.out.println("Customer Registered Successfully!");
                    System.out.println("Generated Customer ID: " + (count + 1));

                    count++;
                    break;

                case 2:
                    System.out.println("\n--- Edit Customer Name ---");

                    System.out.print("Enter Customer ID: ");
                    int idName = sc.nextInt();
                    sc.nextLine();

                    if (idName < 1 || idName > count) {
                        System.out.println("Invalid ID. Try again.");
                        break;
                    }

                    System.out.print("Enter New Name: ");
                    customerNames[idName - 1] = sc.nextLine();

                    System.out.println("Name Updated Successfully!");
                    break;

                case 3:
                    System.out.println("\n--- Check Balance ---");

                    System.out.print("Enter Customer ID: ");
                    int idBal = sc.nextInt();

                    if (idBal < 1 || idBal > count) {
                        System.out.println("Invalid ID. Try again.");
                        break;
                    }

                    System.out.println("Current Balance: ₹" + customerBalances[idBal - 1]);
                    break;

                case 4:
                    System.out.println("\n--- Deposit / Withdraw ---");

                    System.out.print("Enter Customer ID: ");
                    int idUpdate = sc.nextInt();

                    if (idUpdate < 1 || idUpdate > count) {
                        System.out.println("Invalid ID. Try again.");
                        break;
                    }

                    System.out.print("Enter Amount (+ for deposit, - for withdraw): ");
                    double changeAmount = sc.nextDouble();

                    if (customerBalances[idUpdate - 1] + changeAmount < 0) {
                        System.out.println("Insufficient Balance!");
                    } else {
                        customerBalances[idUpdate - 1] += changeAmount;
                        System.out.println("Transaction Successful!");
                    }
                    break;

                case 5:
                    System.out.println("\n------- Account Summary -------");

                    if (count == 0) {
                        System.out.println("No customer records available.");
                        break;
                    }

                    for (int i = 0; i < count; i++) {
                        System.out.println("ID: " + (i + 1) +
                                " | Name: " + customerNames[i] +
                                " | Balance: ₹" + customerBalances[i]);
                    }
                    System.out.println("--------------------------------");
                    break;

                case 6:
                    System.out.println("Exiting CBS... Goodbye!");
                    return;

                default:
                    System.out.println("Invalid Option. Select between 1–6.");
            }
        }
    }
}
