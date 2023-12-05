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
//    vector<int> v(nVals);
//    for (int ii=0; ii<nVals; ++ii) {
//        scanf("%d",&v[ii]);
//    }
    vector<int> v;
    for (int ii=0; ii<nVals; ++ii) {
        int x;
        scanf("%d",&x);
        v.push_back(x);
    }
    
    sort(v.begin(),v.end());
    for (int ii=0; ii<nVals-1; ii++) {
        printf("%d ",v[ii]);
    }
    printf("%d\n",v[nVals-1]);
     
    return 0;
}

