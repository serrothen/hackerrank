import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        
        // read data
        int nL = sc.nextInt();
        List<Integer> arr = new ArrayList<>();
        for (int iEntry=0; iEntry<nL; ++iEntry) {
            int entry = sc.nextInt();
            arr.add(entry);
        }
        
        // read and process queries
        int nQ = sc.nextInt();
        String command;
        for (int iQ=0; iQ<nQ; ++iQ) {
            command = sc.next();
            if (command.equals("Insert")) {
                int x = sc.nextInt();
                int y = sc.nextInt();
                arr.add(x,y);
            } else if (command.equals("Delete")) {
                int x = sc.nextInt();
                arr.remove(x);
            }
        }
        
        // output
        nL = arr.size();
        for (int iEntry=0; iEntry<nL; ++iEntry) {
            System.out.print(arr.get(iEntry)+" ");
        }
        System.out.println();
    }
}
