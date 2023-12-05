import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        // read input
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int ii=0; ii<n; ++ii) {
            a[ii] = sc.nextInt();
        }
        int lenA = a.length;
        int nNegSub = 0;
        // subarray sizes
        for (int isize=1; isize<=lenA; ++isize) {
            // subarray starting entries
            for (int isub=0; isub<=lenA-isize; ++isub) {
                int dummy_sum = 0;
                // entries of subarray
                for (int ientry=0; ientry<isize; ++ientry) {
                    dummy_sum += a[isub+ientry];
                }
                if (dummy_sum<0) {
                    nNegSub += 1;
                }
            }
        }
        
        System.out.println(nNegSub);
    }
}
