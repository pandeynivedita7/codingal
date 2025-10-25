
class Employee {// class blueprint
    int empno;// data member instance variable
    String name;
    float sal;

    // constructor initialize object new keyword automaically 3 types parameter no
    // parameter default
    Employee() {
        System.out.println("*****");
        empno = 101;
        name = "Nivedita Pandey";
        sal = 10000f;
    }

    // method begin execution define function void funname()
    void displayDetails() {
        System.out.println(empno + " | " + name + " | " + sal);
    }
}

class Mainemp {
    public static void main(String[] args) {// entry point

        Employee emp1 = new Employee();
        Employee emp2 = new Employee();
        Employee emp3 = new Employee();

        emp1.displayDetails();
        emp2.displayDetails();
        emp3.displayDetails();
    }
}