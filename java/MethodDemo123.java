class MethodDemo123 {

    // void method
    void showMessage() {
        System.out.println("This is a void method");
    }

    // non-void method
    double Salary() {
        return 25000.50;
    }

    public static void main(String[] args) {
        MethodDemo123 obj = new MethodDemo123();

        obj.showMessage(); // no value returned

        double sal = obj.Salary(); // value returned
        System.out.println("Salary: " + sal);
    }
}
// getter and setter methods for encapsulation inehrtiance parent class will
// make variable as private
