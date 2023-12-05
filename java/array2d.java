import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;



public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        List<List<Integer>> arr = new ArrayList<>();

        int mDim = 6;
        for (int i = 0; i < mDim; i++) {
            String[] arrRowTempItems = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

            List<Integer> arrRowItems = new ArrayList<>();

            for (int j = 0; j < mDim; j++) {
                int arrItem = Integer.parseInt(arrRowTempItems[j]);
                arrRowItems.add(arrItem);
            }

            arr.add(arrRowItems);
        }
        bufferedReader.close();
        
        int hgDim = 3;
        int dummySum = 0;
        int maxSum = -63;
        // upper left corner of hourglass as origin
        for (int irow=0; irow<=mDim-hgDim; ++irow) {
            for (int icol=0; icol<=mDim-hgDim; ++icol) {
                dummySum = arr.get(irow).get(icol)+arr.get(irow).get(icol+1)+arr.get(irow).get(icol+2)
                                                  +arr.get(irow+1).get(icol+1)
                         + arr.get(irow+2).get(icol)+arr.get(irow+2).get(icol+1)+arr.get(irow+2).get(icol+2);
                if (dummySum>maxSum) {
                    maxSum = dummySum;
                }
            }
        }
        System.out.println(maxSum);
    }
}
