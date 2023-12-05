#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int nVals = 0;
    scanf("%d",&nVals);
    vector<int> v(nVals);
    for (int ii=0; ii<nVals; ++ii) {
        scanf("%d",&v[ii]);
    }
    
    int nQ = 0;
    scanf("%d",&nQ);
    for (int ii=0; ii<nQ; ++ii) {
        int iq = 0;
        vector<int>::iterator lower;
        scanf("%d",&iq);
	// returns smallest element in range [v.begin(),v.end())
	// which does not compare less than iq
        lower = std::lower_bound(v.begin(),v.end(),iq);
	// iterator similar to pointer -> de-referencing gives value
        if (*lower==iq) {
            cout << "Yes " << lower-v.begin()+1 << endl;
        } else {
            cout << "No " << lower-v.begin()+1 << endl;        
        }
    }
       
    return 0;
}

