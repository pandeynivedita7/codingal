public class DogTester
{
    public static void main(String[] args)
    {
        Dog d1 = new Dog("Buddy", 4, "Labrador");
        Dog d2 = new Dog("Max", 2);

        d1.displayDog();
        d2.displayDog();
    }
}

class Dog
{
    private String name;
    private int age;
    private String breed;

    // Constructor with 3 parameters
    public Dog(String n, int a, String b)
    {
        name = n;
        age = a;
        breed = b;
    }

    // Constructor with 2 parameters
    public Dog(String n, int a)
    {
        name = n;
        age = a;
        breed = "unknown";
    }

    public void displayDog()
    {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Breed: " + breed);
        System.out.println();
    }
}
