class Student {
    int id;
    String name;
    float stipend;
    // Student(Student other){
    // this.id=other.id
    // this.name=other.name
    // this.stipend=other stipend}

    Student() {// constructors overload method special(automatically object)
        // types student() id=0 string=null stipen=0.0
    } // init object /values/perpare object to use
      // default constructor no parameter passed all defualt

    Student(int id, String name) {// constructor this refernce variable current object in constructor
        this.id = id;// using this same name/same method(constructor)
        this.name = name;// (parameter argument fields)
    }

    Student(int id, String name, float stipend) {
        this.id = id;// 3 parameter
        this.name = name;
        this.stipend = stipend;

    }// types 3
     // default
     // parameter
     // copy constructor manual new object of existing object
     // duplication prevent unwanted effect on orginal

    void displayDetails() {// print formatted string
        System.out.println(this.id + " | " + this.name + " | " + this.stipend);// this current object
    }
} // Student

class MainOverload1 {
    public static void main(String[] args) {
        Student st1 = new Student(); // default constructor
        Student st2 = new Student(45, "jeevika"); // overloaded constructor with 2 parameters
        Student st3 = new Student(234, "Program", 10000);// overloaded constructor with 3 parameters

        st1.displayDetails();
        st2.displayDetails();
        st3.displayDetails();
    }
}