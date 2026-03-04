public class CityArrays {
    public static void main(String[] args) {

        // String array for city names
        String[] cities = { "San Juan", "Accra", "Sao Paulo" };

        // int array for population
        int[] population = { 335468, 2557000, 12330000 };

        // double array for sunshine hours
        double[] sunshine = { 7.5, 6.5, 6.05 };

        // Print information using loop
        for (int i = 0; i < cities.length; i++) {
            System.out.println("City: " + cities[i]);
            System.out.println("Population: " + population[i]);
            System.out.println("Sunshine: " + sunshine[i] + " hrs/day");
            System.out.println(); // blank line
        }
    }
}