import java.io.*;

public class SearchWordInFile {
    public static void main(String[] args) throws IOException {
        String filePath = "input.txt";
        String searchWord = "example";

        BufferedReader br = new BufferedReader(new FileReader(filePath));
        String line;
        int lineNumber = 1;
        boolean found = false;

        while ((line = br.readLine()) != null) {
            if (line.contains(searchWord)) {
                System.out.println("Word found at line: " + lineNumber);
                found = true;
            }
            lineNumber++;
        }
        br.close();

        if (!found) {
            System.out.println("Word not found in the file.");
        }
    }
}