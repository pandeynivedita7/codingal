public class AllDataTypeArrays {
    public static void main(String[] args) {

        // Integer array
        int[] intArray = {10, 20, 30, 40};
        System.out.println("Integer Array:");
        for (int num : intArray) {
            System.out.println(num);
        }

        // Float array
        float[] floatArray = {1.5f, 2.7f, 3.14f};
        System.out.println("\nFloat Array:");
        for (float num : floatArray) {
            System.out.println(num);
        }

        // Double array
        double[] doubleArray = {10.55, 20.66, 30.77};
        System.out.println("\nDouble Array:");
        for (double num : doubleArray) {
            System.out.println(num);
        }

        // String array
        String[] stringArray = {"apple", "banana", "cherry"};
        System.out.println("\nString Array:");
        for (String s : stringArray) {
            System.out.println(s);
        }

        // Boolean array
        boolean[] boolArray = {true, false, true};
        System.out.println("\nBoolean Array:");
        for (boolean b : boolArray) {
            System.out.println(b);
        }

        // Character array
        char[] charArray = {'A', 'B', 'C', 'D'};
        System.out.println("\nCharacter Array:");
        for (char c : charArray) {
            System.out.println(c);
        }

        // Long array
        long[] longArray = {100000L, 200000L, 300000L};
        System.out.println("\nLong Array:");
        for (long l : longArray) {
            System.out.println(l);
        }

        // Short array
        short[] shortArray = {100, 200, 300};
        System.out.println("\nShort Array:");
        for (short s : shortArray) {
            System.out.println(s);
        }

        // Byte array
        byte[] byteArray = {10, 20, 30};
        System.out.println("\nByte Array:");
        for (byte b : byteArray) {
            System.out.println(b);
        }
    }
}
