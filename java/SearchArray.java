public class SearchArray
{
    public static void main(String[] args)
    {
        String[] names = {"Vimudha", "Kandavalli", "Java", "Programming"};
        int i = 0;

        while (i < names.length)
        {
            if(names[i].equals("Java"))
            {
                System.out.println("Target element found at index: " + i);
                break;
            }
            i++;
        }
    }
}