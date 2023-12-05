#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n, s, p, q;
    cin >> n >> s >> p >> q;
    int aOld, aNew;
    vector<int> dict(long(1e8));
    
    aOld = s % long(pow(2,31));
    dict[0] = aOld;
    for (int ii=1; ii<n; ++ii) {
        aNew = aOld * p + q % long(pow(2,31));
        dict[ii] = aNew;
        aOld = aNew;
    }
    
    int nUnique = 0;
    for (int ii=0;ii<long(1e8)-1;++ii) {
        bool unique_flag = true;
        for (int jj=ii+1;jj<long(1e8);++jj) {
            if (dict[ii]==dict[jj]) {
                unique_flag = false;
                break;
            }
        }
        if (unique_flag) nUnique += 1;
    }
    
    cout << nUnique << endl;
    
    return 0;
}
