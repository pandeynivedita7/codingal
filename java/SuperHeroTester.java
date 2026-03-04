// Power class
class Power {
    private String name;
    private int strength;

    public Power(String theName, int theStrength) {
        name = theName;
        strength = theStrength;
    }

    public String getName() {
        return name;
    }

    public int getStrength() {
        return strength;
    }

    public void setStrength(int theStrength) {
        strength = theStrength;
    }
}

// SuperHero class
class SuperHero {
    private String name;
    private Power superPower;

    public SuperHero(String heroName, Power power) {
        name = heroName;

        // Correct initialization (NO aliasing)
        superPower = new Power(power.getName(), power.getStrength());
    }

    public int getStrength() {
        return superPower.getStrength();
    }

    public void setStrength(int strength) {
        superPower.setStrength(strength);
    }
}

// Tester class (ONLY public class)
public class SuperHeroTester {
    public static void main(String[] args) {
        Power speed = new Power("Super Speed", 10);

        SuperHero flash = new SuperHero("The Flash", speed);
        SuperHero shazam = new SuperHero("Shazam", speed);

        System.out.print("Shazam's Strength: ");
        System.out.println(shazam.getStrength());
        System.out.print("Flash's Strength: ");
        System.out.println(flash.getStrength());

        System.out.println("\nUpdating Flash's strength to 15\n");
        flash.setStrength(15);

        System.out.print("Shazam's Strength: ");
        System.out.println(shazam.getStrength());
        System.out.print("Flash's Strength: ");
        System.out.println(flash.getStrength());
    }
}
