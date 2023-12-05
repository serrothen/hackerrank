#include <iostream>
#include <iomanip> 
using namespace std;

int main() {
	int T; cin >> T;
	cout << setiosflags(ios::uppercase);
	cout << setw(0xf) << internal;
	while(T--) {
		double A; cin >> A;
		double B; cin >> B;
		double C; cin >> C;

		/* Enter your code here */
        cout << setw(30) << nouppercase << hex << showbase << left << long(A) << endl;
        cout << setfill('_') << setw(15) << showpos << fixed << setprecision(2) << right << B << endl;
        cout <<  setfill(' ') << noshowpos << setw(30) << uppercase << scientific << setprecision(9) << left << C << endl;

	}
	return 0;

}
