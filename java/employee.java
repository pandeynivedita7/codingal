public class Employee {

    int id;
    String name;
    double salary;

    // Parameterized constructor initializing instance variables
    Employee(int empId, String empName, double empSalary) {
        id = empId;
        name = empName;
        salary = empSalary;
    }

    // Method to display details
    void display() {// does not return any value not use return stamtement
        System.out.println("Employee ID: " + id);
        System.out.println("Employee Name: " + name);
        System.out.println("Employee Salary: " + salary);
    }

    // Main method
    public static void main(String[] args) {
        // Passing values to constructor
        Employee e1 = new Employee(101, "Rahul", 45000.50);
        Employee e2 = new Employee(102, "Priya", 52000.75);

        e1.display();
        System.out.println("------------------");
        e2.display();
    }
}

public String toString() {
    return "Employee [id=" + id + ", name=" + name + ", salary=" + salary + "]";
}

public int addBonus(int bonus) {
    return (int) (salary + bonus);
}