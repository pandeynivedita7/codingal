class Mainstring {
    public static void main(String[] args) {
        // user input process can also be used rather than giving manual inputs
        String first = "Nivedita";
        String second = "Pandey";
        String codingal = first + second;
        String codingalTrick = "Welcome" + "to" + " Nivedita class";
        String codingalCapital = codingal.toUpperCase();
        String codingalSmall = codingalCapital.toLowerCase();
        // correct spelling is length not lenght
        int lengthOfCodingal = codingal.length();// number
        int lengthOfCodingalTrick = codingalTrick.length();// number
        int sum = lengthOfCodingal + lengthOfCodingalTrick;

        // Guess the answer before running
        // a msg can also be added for the output screen if required
        System.out.println(codingal);
        System.out.println(codingalTrick);
        System.out.println(codingalCapital);
        System.out.println(codingalSmall);
        System.out.println(sum);

        // strings method
        // + join 2 string
        // toLowerCase()
        // toUpperCase()
        // length() number of char in given string int
        // . operator .length()
        // .toLowerCase
        // .toUpperCase
        // .methods()

    }
}