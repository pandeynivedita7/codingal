class FinalPriceCalculator {
    public static void main(String[] args) {

        // Original price of the item
        double originalPrice = 1000.0;

        // Discount percentage (e.g., 10% discount)
        double discountPercentage = 10.0;

        // Sales tax percentage (e.g., 5% tax)
        double salesTaxPercentage = 5.0;

        // Calculate discount amount
        double discountAmount = (originalPrice * discountPercentage) / 100;

        // Price after discount
        double priceAfterDiscount = originalPrice - discountAmount;

        // Calculate tax amount
        double taxAmount = (priceAfterDiscount * salesTaxPercentage) / 100;

        // Final price
        double finalPrice = priceAfterDiscount + taxAmount;

        // Output result
        System.out.println("Original Price: " + originalPrice);
        System.out.println("Discount Amount: " + discountAmount);
        System.out.println("Price After Discount: " + priceAfterDiscount);
        System.out.println("Tax Amount: " + taxAmount);
        System.out.println("Final Price: " + finalPrice);
    }
}
