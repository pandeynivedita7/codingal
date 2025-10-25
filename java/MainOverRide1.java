class Parent {
    public void sayHello() {
        System.out.println("Hello from Parent");
    }// method overriding specific method of sub class taken from super class already
     // defined
}// same name same parmeter same return type
 //

class Child extends Parent {
    @Override
    public void sayHello() {
        System.out.println("Hello from Chid");
    }
}

class MainOverRide1 {
    public static void main(String[] args) {
        // Parent p = new Child(); // for calling hello from child
        Parent p = new Parent(); // for calling hello from parent
        p.sayHello();
    }
}
