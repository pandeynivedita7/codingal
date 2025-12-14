class Car {
    String brand;   // field
    int speed;      // field
    // constructor required to call object initialization of variables 
    // rule constructor name same as class name
    // no return type not even void
    
    public Car(String carBrand, int carSpeed) {
        brand = carBrand;// nickname this optional
        speed = carSpeed;
    }

    public Car() {// default constructor
        brand = "Unknown";
        speed = 0;
    }

// type of constructor : default constructor(no argument) parameterized constructor(with argument)
   public/void drive() {  // method behaviour action
         return// void never returns value
         System.out.println(brand + " is driving");
    }
}
// class name object name=new class name();
car suv=new car();// object creation
car sedan=new car();
sedan.brand="honda";
sedan.speed=80;

//class:car  object:suv
suv.brand="toyota";// access anything you have to do it using object
suv.speed=100;
