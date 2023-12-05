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
    int pos = 0;
    scanf("%d",&pos);
    v.erase(v.begin()+pos-1);
    
    int lower = 0;
    int upper = 0;
    scanf("%d",&lower);
    scanf("%d",&upper);
    v.erase(v.begin()+lower-1,v.begin()+upper-1);
    
    int len = v.size();
    printf("%d\n",len);
    if (len>1) {
        for (int ii=0; ii<len-1; ++ii) {
            printf("%d ", v[ii]);
            }
    }
    printf("%d\n",v[len-1]);
    
    return 0;
}

