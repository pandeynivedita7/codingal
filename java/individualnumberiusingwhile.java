int num = 345;

while (num > 0) {
  // get the first digit by using the mod function
  int digit = num % 10;
  System.out.println(digit);

  // Divide the number by 10
  num /= 10; // Integer division truncates the number
}