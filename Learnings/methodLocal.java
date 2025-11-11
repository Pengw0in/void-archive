public class methodLocal {
    static void methodLocalImple(){
        class testing{
            void run(){
                System.out.println("HI!");
            }
        }

        testing test = new testing();
        test.run();
    }
    public static void main(String[] args) {
        methodLocalImple();
    }
}
