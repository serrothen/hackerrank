import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String B=sc.next();
        /* Enter your code here. Print output to STDOUT. */
        int sum_len = A.length()+B.length();
        System.out.println(sum_len);
        if (A.compareTo(B)>0) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
        
        String capitalA = A.substring(0,1).toUpperCase()+A.substring(1);
        String capitalB = B.substring(0,1).toUpperCase()+B.substring(1);
        System.out.println(capitalA+" "+capitalB);
        
        //String rootA = A.substring(0,1);
        //String trailA = A.substring(1);
        //String rootB = B.substring(0,1);
        //String trailB = B.substring(1);
        //System.out.println(rootA.toUpperCase()+trailA+" "+rootB.toUpperCase()+trailB);
        
    }
}
