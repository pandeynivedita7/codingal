public class EvenIndexExample
{
    public static void main(String[] args)
    {
        // Create array
        int[] arr = {10, 20, 30, 40};

        // Access even indices
        for(int i = 0; i < arr.length; i += 2)
        {
            System.out.println("Index: " + i + " Value: " + arr[i]);
        }
    }
}