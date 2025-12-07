class carstringconcatenation {
    String brand;
    int speed;

    carstringconcatenation(String b, int s) {
        brand = b;
        speed = s;
    }

    String getInfo() {
        return "Brand: " + brand + ", Speed: " + speed + "km/h";
    }
}

class Main {
    public static void main(String[] args) {
        carstringconcatenation car1 = new carstringconcatenation("Toyota", 180);
        carstringconcatenation car2 = new carstringconcatenation("bmw", 240);

        System.out.println(car1.getInfo());
        System.out.println(car2.getInfo());
    }
}