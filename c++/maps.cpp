#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int nQ = 0;
    scanf("%d",&nQ);
    
    map<string,int> classbook;
    
    for (int iq=0; iq<nQ; ++iq) {
        int type = 0;
        string name = "";
        int mark = 0;

        scanf("%d",&type);
        if (type==1) {
	    // read
            cin >> name >> mark;
            // search
            map<string,int>::iterator itr = classbook.find(name);

            if (itr != classbook.end()) {
		// sum up marks
                classbook[name] += mark;
            } else {
		// add student
                classbook.insert(make_pair(name,mark));
            }
        } else if (type==2) {
	    // read
            cin >> name;
	    // remove student
            classbook.erase(name);
        } else if (type==3) {
	    // read
            cin >> name;
	    // search
            map<string,int>::iterator itr = classbook.find(name);
	    // output
            if (itr != classbook.end()) {
                cout << itr->second << endl;
            } else {
                cout << 0 << endl;
            }
        }
    }
      
    return 0;
}
