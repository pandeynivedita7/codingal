
//this is known as pojo class -plain old java object
import java.util.Scanner;

public class GetSet {
    public static Employee getEmployeeDetails() {

        Scanner scanner = new Scanner(System.in);
        int id;
        String name;
        double salary;
        // driver input
        System.out.println("Enter Id:");
        id = scanner.nextInt();

        System.out.println("Enter Name:");
        name = scanner.next();

        System.out.println("Enter salary:");
        salary = scanner.nextDouble();

        Employee employee = new Employee();
        employee.setEmployeeId(id);
        employee.setEmployeeName(name);
        employee.setSalary(salary);

        return employee;
    }

    public static int getPFPercentage() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter PF percentage:");
        return scanner.nextInt();
    }

    public static void main(String[] args) {
        // driver program
        Employee employee = getEmployeeDetails();
        int pfp = getPFPercentage();
        employee.calculateNetSalary(pfp);

        System.out.println("Id : " + employee.getEmployeeId());
        System.out.println("Name : " + employee.getEmployeeName());
        System.out.println("Salary : " + employee.getSalary());
        System.out.println("net Salary : " + employee.getNetSalary());
    }
}

public class Employee {
    private int employeeId;
    private String employeeName;
    private double salary;
    private double netSalary;

    public int getEmployeeId() {
        return employeeId;
    }

    public void setEmployeeId(int employeeId) {
        this.employeeId = employeeId;
    }

    public String getEmployeeName() {
        return employeeName;
    }

    public void setEmployeeName(String employeeName) {
        this.employeeName = employeeName;
    }

    public double getSalary() {
        return salary;
    }

    public void setSalary(double salary) {
        this.salary = salary;
    }

    public double getNetSalary() {
        return netSalary;
    }

    public void setNetSalary(double netSalary) {
        this.netSalary = netSalary;
    }

    public void calculateNetSalary(int pfPercentage) {
        double pf = salary * (double) pfPercentage / 100.0;// deductions in salary can also be added in logic here
        netSalary = salary - pf;
    }
}
