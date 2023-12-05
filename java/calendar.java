import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

class Result {

    /*
     * Complete the 'findDay' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts following parameters:
     *  1. INTEGER month
     *  2. INTEGER day
     *  3. INTEGER year
     */

    public static String findDay(int month, int day, int year) {
        Calendar cal = Calendar.getInstance();
        
        // months start at 0
        cal.set(Calendar.MONTH,month-1);
        cal.set(Calendar.DAY_OF_MONTH,day);
        cal.set(Calendar.YEAR,year);
        
        System.out.println(Calendar.MONTH);
        System.out.println(Calendar.DAY_OF_MONTH);
        System.out.println(Calendar.YEAR);
        
        int weekday;
        weekday = cal.get(Calendar.DAY_OF_WEEK);
        System.out.println(weekday);
        
        if (weekday==1) {
            return "SUNDAY";
        } else if (weekday==2) {
            return "MONDAY";
        } else if (weekday==3) {
            return "TUESDAY";
        } else if (weekday==4) {
            return "WEDNESDAY";
        } else if (weekday==5) {
            return "THURSDAY";
        } else if (weekday==6) {
            return "FRIDAY";
        } else {
            return "SATURDAY";
        }
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int month = Integer.parseInt(firstMultipleInput[0]);

        int day = Integer.parseInt(firstMultipleInput[1]);

        int year = Integer.parseInt(firstMultipleInput[2]);

        String res = Result.findDay(month, day, year);

        bufferedWriter.write(res);
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}

