//this activity is mainly to undersand the concept of inheritance
//Parent Class
class Parent {
    int age, id;// instance variable age id name
    String name;

    void naming(String name)// method naming performance string print name void doesnt return value
    {
        System.out.println("Name:" + name);
    }
}

// child class
class Child extends Parent {// method naming variable age id and name
    void ageN(int age) {// method ageN
        System.out.println("Age of student is:" + age);
    }
}

class Student {
    public static void main(String[] er) {// variable name
        Child s = new Child();// creating object of child class
        s.naming("Nivedita");// classname objectname=new classname() call method from parent class
        s.ageN(30);// call method child
    }

}
// public static void main(String[] args)

// public static void main(String[] er)

// public static void main(String[] input)

/*
 * class and object
 * reuse car
 * class blueprint 2 types properties and behaviour
 * class dog contains variable 4 legs 1 tail colour etc behaviour(method) loyal
 * etc contructor
 */