import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        /* Enter your code here. Print output to STDOUT. */
        char[] Achar = A.toCharArray();
        int lenA = A.length();
        String response = "Yes";
        
        for (int ii=0; ii<=lenA/2; ++ii) {
            if (Achar[ii]!=Achar[lenA-ii-1]) {
                response = "No";
                break;
            }
        }
        
        System.out.println(response);
        
    }
}
