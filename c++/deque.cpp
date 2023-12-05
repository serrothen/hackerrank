#include <iostream>
#include <deque> 
using namespace std;

void printKMax(int arr[], int n, int k){
	//Write your code here.
    deque<int> window;
    int max_val = 0;
    for (int ii=0; ii<k; ++ii) {
        if (arr[ii]>max_val) max_val = arr[ii];
        window.push_back(arr[ii]);
    }
    cout << max_val << " ";
    for (int ii=k; ii<n; ++ii) {
        if (window.front()==max_val) {
            max_val = 0;
            for (auto it=window.begin()+1; it!=window.end(); ++it) {
                if (*it>max_val) max_val = *it;
            }
        }
        window.pop_front();
        window.push_back(arr[ii]);
        if (window.back()>max_val) max_val = window.back();
        cout << max_val << " ";
    }
    cout << endl;
}

int main(){
  
	int t;
	cin >> t;
	while(t>0) {
		int n,k;
    	cin >> n >> k;
    	int i;
    	int arr[n];
    	for(i=0;i<n;i++)
      		cin >> arr[i];
    	printKMax(arr, n, k);
    	t--;
  	}
  	return 0;
}
