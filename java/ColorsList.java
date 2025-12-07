import java.util.ArrayList;

public class ColorsList {
    public static void main(String[] args) {
        ArrayList<String> colors = new ArrayList<>();

        colors.add("Red");
        colors.add("Blue");
        colors.add("Green");
        if (names.contains("Blue")) {
            System.out.println("Emma is in the list");
        } else {
            System.out.println("Emma is NOT in the list");
        }

        System.out.println("Colors: " + colors);

        colors.remove("Blue");
        System.out.println("After removing Blue: " + colors);

        System.out.println("Second color: " + colors.get(1));

        System.out.println("Size: " + colors.size());

    }
}// method add get set remove size contains clear isEmpty
