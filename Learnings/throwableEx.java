public class throwableEx {
    static void validate(int age){
        if(age < 18){
            throw new ArithmeticException("not valid");
        } else{
            System.out.println("Welcome to voting");
        }
    }
    public static void main(String[] args) {
        validate(12);
    }
}
