import java.util.Scanner;

public class Solution {

    public static String getSmallestAndLargest(String s, int k) {
        String smallest = "";
        String largest = "";
        
        // Complete the function
        // 'smallest' must be the lexicographically smallest substring of length 'k'
        // 'largest' must be the lexicographically largest substring of length 'k'
        int lenS = s.length();
	// must initialize "smallest", since otherwise an empty string remains
        smallest = s.substring(0,k);
        String dummySub;
        for (int ii=0; ii<=lenS-k; ++ii) {
            dummySub = s.substring(ii,ii+k);
            if (smallest.compareTo(dummySub)>0) {
                smallest = dummySub;
            }
            if (largest.compareTo(dummySub)<0) {
                largest = dummySub;
            }
        }
        
        return smallest + "\n" + largest;
    }


    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();
      
        System.out.println(getSmallestAndLargest(s, k));
    }
}
