import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        
        // read number of datasets
        int nLines = sc.nextInt();
        // read list of datasets
        List<List<Integer>> arr = new ArrayList<>();
        for (int iLine=0; iLine<nLines;++iLine) {
            int nEntries = sc.nextInt();
            // read one dataset
            List<Integer> arrRowItems = new ArrayList<>();
            for (int iEntry=0; iEntry<nEntries; ++iEntry) {
                int arrItem = sc.nextInt();
                arrRowItems.add(arrItem);  
            }
            arr.add(arrRowItems);
        }
        
        // read number of queries
        int nQ = sc.nextInt();
        // read and perform queries
        for (int iQ=0; iQ<nQ; ++iQ) {
            // query
            int x = sc.nextInt();
            int y = sc.nextInt();
            // check if query in range of data
            if (x<arr.size()+1) {
                if (y<arr.get(x-1).size()+1) {
                    System.out.println(arr.get(x-1).get(y-1));
                } else {
                    System.out.println("ERROR!");
                }
            } else {
                System.out.println("ERROR!");
            }
        }
    }
}
