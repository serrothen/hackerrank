import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            int seq = a;
            int addend = b;
            for (int jj=0; jj<n; ++jj) {
                seq += addend;
                addend *= 2;
                System.out.print(String.format("%d ",seq));
            }
            System.out.print("\n");
        }
        in.close();
    }
}
