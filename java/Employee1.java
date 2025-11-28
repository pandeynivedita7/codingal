public class Employee1 {// blueprint for employee object

    int id;// instance variable
    String name;
    double salary;

    // Parameterized constructor initializing instance variables
    Employee(int empId, String empName, double empSalary) {// allocating , initializing memory
        id = empId;// 2 types 1 with parameter 2 without parameter
        name = empName;// IF YOU DO NOT PROVIDE A CONSTRUCTOR JAVA PROVIDES A DEFAULT CONSTRUCTOR
        salary = empSalary;
    }

    // Method to display details behavior
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
        // class name object name = new class name (parameters if any);
        // Displaying employee details
        e1.display();
        System.out.println("------------------");
        e2.display();
    }
}

public String toString() {// use it to return string representation of object system defined method
    return "Employee [id=" + id + ", name=" + name + ", salary=" + salary + "]";
}

public int addBonus(int bonus) {// user defined method
    return (int) (salary + bonus);
    // e2.addBonus(5000);
    // SOPL("Salary after bonus: "+e2.addBonus(5000));
}// access modifier (public/private) datatype methodname(parameter list){body
 // return type;} method signature