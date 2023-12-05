#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.
    int a, b;
    scanf("%d", &a);
    scanf("%d", &b);
    
    for (int ii=a; ii<=b; ++ii) {
        if (ii==1) {
            printf("one\n");
        }
        else if (ii==2) {
            printf("two\n");
        }
        else if (ii==3) {
            printf("three\n");
        }
        else if (ii==4) {
            printf("four\n");
        }
        else if (ii==5) {
            printf("five\n");
        }
        else if (ii==6) {
            printf("six\n");
        }
        else if (ii==7) {
            printf("seven\n");
        }
        else if (ii==8) {
            printf("eight\n");
        }
        else if (ii==9) {
            printf("nine\n");
        }
        if (ii>9 && ii%2==0) {
            printf("even\n");
        }
        if (ii>9 && ii%2!=0) {
            printf("odd\n");
        }
    }
    
    return 0;
}
