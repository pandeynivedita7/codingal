public class Cat {
    String name;
    int age;

    public Cat() {
        name = "Unknown";
        age = 0;
    }

    public Cat(String n, int a) {
        name = n;
        age = a;
    }

    public void display() {
        System.out.println("Name: " + name + ", Age: " + age);
    }
}
