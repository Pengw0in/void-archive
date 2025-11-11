interface Greeting {
    void greet();
}

public class anonymousImple {
    public static void main(String[] args) {
        Greeting anon = new Greeting() {
            @Override
            public void greet(){
                System.out.println("HI!");
            }
        };
        anon.greet();
    }
}
