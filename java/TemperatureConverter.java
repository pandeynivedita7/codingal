// TemperatureConverter.java
// A simple program to convert Celsius to Fahrenheit and Fahrenheit to Celsius
// Demonstrates variable manipulation and typecasting

public class TemperatureConverter {
    public static void main(String[] args) {
        // Step 1: Declare integer variables
        int celsius = 30; // temperature in Celsius
        int fahrenheit = 86;
        // String num = "123";
        // String num1 = "456";
        // String sum = (int) num + num1;
        // temperature in Fahrenheit

        // Step 2: Convert Celsius to Fahrenheit using typecasting
        double convertedToFahrenheit = ((double) celsius * 9 / 5) + 32;

        // Step 3: Convert Fahrenheit to Celsius using typecasting
        double convertedToCelsius = ((double) (fahrenheit - 32) * 5 / 9);

        // Step 4: Display results
        System.out.println("=== Temperature Converter ===");
        System.out.println("Celsius temperature (int): " + celsius);
        System.out.println("Converted to Fahrenheit (double): " + convertedToFahrenheit);

        System.out.println("\nFahrenheit temperature (int): " + fahrenheit);
        System.out.println("Converted to Celsius (double): " + convertedToCelsius);
        // System.out.println(sum);
    }
}
