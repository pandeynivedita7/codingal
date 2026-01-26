class MethodOverloadingDisplay {

    void show(int a) {// doesnt has return type
        System.out.println("Integer value: " + a);
    }

    void show(String a) {
        System.out.println("String value: " + a);
    }

    public static void main(String[] args) {
        MethodOverloadingDisplay obj = new MethodOverloadingDisplay();
        obj.show(100);
        obj.show("Hello Java");
    }
}
