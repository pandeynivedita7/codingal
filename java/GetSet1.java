class Student {
    // 1. Private variables (data hiding)
    private String name;
    private int age;

    // 2. Public getters and setters (controlled access)
    public String getName() {
        return name;
    }

    public void setName(String name) {
        // Optional: Validation
        if (!name.isEmpty()) {// is my name is not empty
            this.name = name;
        }
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        if (age > 0) {
            this.age = age;
        }
    }
}

public class GetSet1 {
    public static void main(String[] args) {
        Student s = new Student();
        s.setName("Swapnil");
        s.setAge(25);

        System.out.println(s.getName() + " is " + s.getAge() + " years old.");
    }
}
