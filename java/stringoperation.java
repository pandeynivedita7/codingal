String s="javaprogramming";// string variable=value;
System.out.println(s.length());//s.length() returns length of string
System.out.println(s.toUpperCase());// converts to uppercase
System.out.println(s.toLowerCase());// converts to lowercase
System.out.println(s.charAt(1));// prints 'a'  charAt(index)
System.out.println(s.substring(1,3));// prints 'av'
System.out.println(s.substring(3));//aprogramming only 1 parameter starts from index 3 to end
System.out.println("Hello".equals("Hello"));          // true output true and false are boolean values
System.out.println("Hello".equals("hello"));          // false
System.out.println("hello".equalsIgnoreCase("HELLO")) // true

String s="banana";
System.out.println(s.indexOf('a')); //1 
System.out.println(s.lastIndexOf('a')); //5
System.out.println(s.indexOf("na")); //2 uses substring
System.out.println(s.indexOf('x')); //-1 character not found
System.out.println("Java".replace('a', 'o')); // Jovo replace(source char, target char )
System.out.println("a1b2c3".replaceAll("\\d", "*")); // a*b*c* \\d represents digits
System.out.println("  Hello World  ".trim()); // "Hello World" removes leading and trailing spaces
System.out.println("Hello" + " " + "World"); // Hello World

String s = "program";
System.out.println(s.startsWith("pro")); // true
System.out.println(s.endsWith("gram"));  // true
System.out.println(s.contains("gra"));   // true