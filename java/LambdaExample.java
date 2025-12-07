import java.util.ArrayList;

public class LambdaExample {
  public static void main(String[] args) {
	System.out.println("==========Lambdas=======");
    ArrayList<Integer> numbers = new ArrayList<Integer>();
    numbers.add(35);
    numbers.add(48);
	//numbers.add(49);
    numbers.add(18);
    numbers.add(13);// lambda expression function action to be performed
    numbers.forEach( (x) -> { System.out.println(x); } );// for int conditional action inc and de
	numbers.forEach(n -> { if (n == 49) System.out.println("Found 49");
							 });
  }
}