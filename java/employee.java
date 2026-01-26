public class Employee {// creating class Employee

    int id;// instance variable
    String name;
    double salary;

    // Parameterized constructor initializing instance variables
    Employee(int empId, String empName, double empSalary) {// initialize instance variables
        id = empId;
        name = empName;
        salary = empSalary;
    }

    // Method to display details  metgod behaviour
    void display() {// does not return any value not use return stamtement
        System.out.println("Employee ID: " + id);
        System.out.println("Employee Name: " + name);
        System.out.println("Employee Salary: " + salary);
    }

    // Main method
    public static void main(String[] args) {// create object of Employee class keyword new
        // Passing values to constructor
        Employee e1 = new Employee(101, "Rahul", 45000.50);
        Employee e2 = new Employee(102, "Priya", 52000.75);
        // int name;
        e1.display();// call method
        System.out.println("------------------");
        e2.display();
    }
}

public String toString() {// defualt method of object class display a string representation of object
    return "Employee [id=" + id + ", name=" + name + ", salary=" + salary + "]";
}

public int addBonus(int bonus) {// created a method to add bonus to salary
    return (int) (salary + bonus);
}