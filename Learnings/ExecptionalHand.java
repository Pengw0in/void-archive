public class ExecptionalHand {
    public static void main(String[] args) {
        try{
            int arr[] = new int[2];
            arr[1] = '#';
        } catch(ArithmeticException e){
            System.out.println("Invalid division");
        } catch(ArrayIndexOutOfBoundsException e){
            System.out.println("You suck at counting");
        } catch(Exception e){
            System.out.println("Unkonwn error");
        } finally{
            System.out.println("done");
        }
    }
}