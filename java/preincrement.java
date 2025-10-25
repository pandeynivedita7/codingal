/*Pre-increment (++x): Increases value by 1, then uses the updated value.

Post-increment (x++): Uses the current value, then increases by 1.

Pre-decrement (--x): Decreases value by 1, then uses the updated value.

Post-decrement (x--): Uses the current value, then decreases by 1.*/

int a = 5;
System.out.println(++a);  // 6 (pre-increment: first increase, then print)
System.out.println(a++);  // 6 (post-increment: print first, then increase to 7)
System.out.println(--a);  // 6 (pre-decrement: decrease to 6, then print)
System.out.println(a--);  // 6 (post-decrement: print first, then decrease to 5)


int x = 10;
int y = ++x + x++ + --x + x--;//x=11 use 11 then x=12 x=11 use 11 use 11 then x=10
System.out.println("x = " + x); // Final value?x=10
System.out.println("y = " + y); // Value? y=44


for (int i = 0; i <=5; i++) {
    System.out.print(i + " ");  // 0 1 2 3 4 5
}

int i = 0;
while (++i <= 5) {
    System.out.print(i + " "); //1 2 3 4 5
}

int a = 3;
int b = a++ + ++a + --a + a--;// use 3 then a=4 a=5 use 5 a=4 use 4 use 4 a=3  3+5+4+4=16
System.out.println(a + ", " + b);//a=3 b=16

int x = 5, y = 7;
int z = x++ + --y + y++ + ++x;
System.out.println("x=" + x + ", y=" + y + ", z=" + z);

int p = 1;
p = p++ + ++p + p++ + --p;
System.out.println(p);

int a = 2;
int b = ++a + a++ + --a + a--;
System.out.println("a=" + a + ", b=" + b);
