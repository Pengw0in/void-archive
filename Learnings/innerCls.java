class outer{
    private String mess = "HI!";
    class inner{
        void innerMethod(){
            System.out.println(mess);
        }
    }

    void runInner(){
        inner in = new inner();
        in.innerMethod();
    }
}

public class innerCls {
    public static void main(String[] args) {
        outer out = new outer();
        out.runInner();
    }
}
