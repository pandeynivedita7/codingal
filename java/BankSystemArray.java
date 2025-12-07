import java.util.Scanner;

public class BankSystemArray {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        String[] names = new String[100]; // store customer names
        double[] balances = new double[100]; // store customer balances
        int totalCustomers = 0;
        /*
         * String line = sc.nextLine();
         * int n = sc.nextInt();
         * double d = sc.nextDouble();
         * float f = sc.nextFloat();
         * boolean b = sc.nextBoolean();
         */

        while (true) {
            System.out.println();
            System.out.println("Select any one option from below.");
            System.out.println("1-> Add Customer");
            System.out.println("2-> Change Customer Name");
            System.out.println("3-> Check Account Balance");
            System.out.println("4-> Update Account Balance");
            System.out.println("5-> Summary of All Accounts");
            System.out.println("6-> Quit");
            System.out.print("Enter your option to proceed ahead: ");

            int choice = sc.nextInt();
            sc.nextLine(); // clear buffer

            switch (choice) {

                case 1:
                    System.out.println("\nAdd Customer");

                    System.out.print("Enter Customer Name: ");
                    names[totalCustomers] = sc.nextLine();

                    System.out.print("Enter Opening Balance Amount: ");
                    balances[totalCustomers] = sc.nextDouble();

                    System.out.println("Account created successfully.");

                    totalCustomers++;
                    break;

                case 2:
                    System.out.print("\nEnter Customer ID (1 - " + totalCustomers + "): ");
                    int id2 = sc.nextInt();
                    sc.nextLine();

                    if (id2 < 1 || id2 > totalCustomers) {// Customer ID must be at least 1.Customer ID cannot be
                                                          // greater than the number of customers currently stored.
                        System.out.println("Invalid Customer ID.");
                        break;
                    }

                    System.out.print("Enter new Customer Name: ");
                    names[id2 - 1] = sc.nextLine();

                    System.out.println("Name updated successfully.");
                    break;

                case 3:
                    System.out.print("\nEnter Customer ID (1 - " + totalCustomers + "): ");
                    int id3 = sc.nextInt();

                    if (id3 < 1 || id3 > totalCustomers) {
                        System.out.println("Invalid Customer ID.");
                        break;
                    }

                    System.out.println("Account Balance: " + balances[id3 - 1]);
                    break;

                case 4:
                    System.out.print("\nEnter Customer ID (1 - " + totalCustomers + "): ");
                    int id4 = sc.nextInt();

                    if (id4 < 1 || id4 > totalCustomers) {
                        System.out.println("Invalid Customer ID.");
                        break;
                    }

                    System.out.print("Enter amount to add (negative to deduct): ");
                    double amt = sc.nextDouble();

                    balances[id4 - 1] += amt;

                    System.out.println("Balance updated successfully.");
                    break;

                case 5:
                    System.out.println("\nSummary of All Accounts:");
                    for (int i = 0; i < totalCustomers; i++) {
                        System.out.println("ID: " + (i + 1) +
                                " | Name: " + names[i] +
                                " | Balance: " + balances[i]);
                    }
                    break;

                case 6:
                    System.out.println("Exiting Program...");
                    return;

                default:
                    System.out.println("Invalid option. Try again.");
            }
        }
    }
}
