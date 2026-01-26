class Employee {
    int empId;
    String empName;
    double salary;

    // Default constructor
    Employee() {
        empId = 0; // fixed default value
        empName = "Vimudha";
        salary = 0.0;
    }

    // User-defined method
    void display() {
        System.out.println("Employee ID: " + empId);
        System.out.println("Employee Name: " + empName);
        System.out.println("Salary: " + salary);
    }
}

public class EmployeeDefaultConstructor {
    public static void main(String[] args) {
        // Object creation – default constructor is called
        Employee e1 = new Employee(); // new keyword creates object
        e1.display(); // method call
    }
}
