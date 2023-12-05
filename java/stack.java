import java.util.*;
class Solution{
	
	public static void main(String []argh)
	{
		Scanner sc = new Scanner(System.in);
		
		while (sc.hasNext()) {
			String input=sc.next();
            //Complete the code
            Stack<Character> stack = new Stack<>();
            int lenInput = input.length();
            char[] arr = input.toCharArray();
            
            for (int iarr=0; iarr<lenInput; ++iarr) {
                if (arr[iarr]=='(' || arr[iarr]=='[' || arr[iarr]=='{') {
                    stack.push(arr[iarr]);
                } else {
                    if (!stack.empty()) {
                        if ( (stack.peek()=='(' && arr[iarr]==')') ||
                             (stack.peek()=='[' && arr[iarr]==']') ||
                             (stack.peek()=='{' && arr[iarr]=='}') ) {
                                stack.pop();
                        } else {
                            break;
                        }
                    } else {
                        stack.push(arr[iarr]);
                        break;
                    }
                }
            }
            
            if (stack.empty()) {
                System.out.println("true");
            } else {
                System.out.println("false");
            }
            
		}
		
	}
}
