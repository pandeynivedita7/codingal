class Test {

    void print(int a, String b) {
        System.out.println(a + " " + b);
    }

    void print(String b, int a) {
        System.out.println(b + " " + a);
    }

    public static void MethodOverloadingTest(String[] args) {
        Test t = new Test();
        t.print(10, "Java");
        t.print("Java", 10);
    }
}
