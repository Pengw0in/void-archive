import java.util.ArrayList;
import java.util.Vector;

public class arrlst {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();

        list.add("Hello");
        list.add("Guave");
        list.add("apple");

        int index = list.indexOf("apple");
        System.out.println(list.indexOf("apple"));
        System.out.println(list);
        list.clear();
        System.out.println(list);        


        

    }
}