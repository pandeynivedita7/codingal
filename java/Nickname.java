public class Nickname {
    private String firstName;
    private String lastName;
    private String nickname;

    public Nickname(String realFirstName, String realLastName, String moniker) {
        firstName = realFirstName;
        lastName = realLastName;
        nickname = moniker;
    }

    public void setNickName(String newNickname) {
        nickname = newNickname;
    }

    public String toString() {
        return firstName + " (" + nickname + ") " + lastName;
    }
}

public class MyProgram {
    public static void main(String[] args) {
        Nickname karel = new Nickname("Karel", "Dog", "the Dog");
        Nickname dwayne = new Nickname("Dwayne", "Johnson", "the Rock");
        Nickname travis = new Nickname("Travis", "Fish", "Redfinn");

        System.out.println(karel);
        System.out.println(dwayne);
        System.out.println(travis);

        System.out.println();

        System.out.println(karel + " went to a movie with " + travis);
    }
}
