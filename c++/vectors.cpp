#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    // get repetitions
    int n_vals = 0;
    int n_queries = 0;
    scanf("%d",&n_vals);
    scanf("%d",&n_queries);

    // container of containers    
    vector<vector<int>> a(n_vals);
    
    // read in data
    for (int ii=0; ii<n_vals; ++ii) {
	// number of entries
        int nk = 0;
        scanf("%d",&nk);
	// read in vector on one line
        vector<int> b(nk);
        for (int jj=0; jj<nk; ++jj) {
            scanf("%d",&b[jj]);
        }
	// move data
        a[ii] = std::move(b);
    }
    
    for (int iq=0; iq<n_queries; ++iq) {
	// location
        int i_outer = 0;
        int i_inner = 0;
        scanf("%d",&i_outer);
        scanf("%d",&i_inner);
	// output
        printf("%d\n",a[i_outer][i_inner]);
    }
       
    return 0;
}
