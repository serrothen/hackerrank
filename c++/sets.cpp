#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int nQ = 0;
    scanf("%d",&nQ);
    
    set<int> st;
    for (int ii=0; ii<nQ; ++ii) {
        int x, q;
        scanf("%d %d",&q,&x);
        
        if (q==1) {
            st.insert(x);
        } else if (q==2) {
            st.erase(x);
        } else if (q==3) {
            set<int>::iterator itr = st.find(x);
	    // check if integer found
            if (itr != st.end()) {
                printf("Yes\n");
            } else {
                printf("No\n");
            }
        }
        
    }
       
    return 0;
}
