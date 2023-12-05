#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int num=0;
    scanf("%d",&num);
    int arr[num];
    for (int ii=0; ii<num; ++ii) {
        scanf("%d",&arr[ii]);
    }
    for (int ii=num-1;ii>0; --ii) {
        printf("%d ",arr[ii]);
    }
    printf("%d",arr[0]);
    
    return 0;
}

