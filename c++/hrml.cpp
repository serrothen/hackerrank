#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    
    int nMarkup,nQ;
    cin >> nMarkup >> nQ;
    cin.get(); // get rid of newline

    // containers for tags, attribute names and values
    vector<string> tagList(nMarkup);
    vector<vector<string>> attrNameList(nMarkup);
    vector<vector<string>> attrValList(nMarkup);

    // storage for nested tags
    string tagNest {""};
    // read source    
    for (int ii=0; ii<nMarkup; ++ii) {
	// get line
	string str {""};
        getline(cin,str);

	bool tagFlag {true};
	bool attrValFlag {false};
	bool skipSpace {false};
	string buff {""};
	for (auto s : str) {
	    // get tag
	    if (tagFlag) {
	       if (s!='<' && s!=' ' && s!='>') {
	          buff+=s;
	       } else if (s==' ') {
		  // add tag to storage
		  if (tagNest=="") {
	             tagNest += buff;
		  } else {
		     tagNest += "."+buff;
		  }
	          tagList[ii] = tagNest;
	          buff = "";
	          tagFlag = false;
		  continue;
	       } else if (s=='>') {
		  // remove tag from storage
		  if (buff[0]=='/') {
		     for (auto it=tagNest.rbegin(); it!=tagNest.rend(); ++it) {
		         if (*it!='.') {
			    tagNest.pop_back();
			 } else {
			    tagNest.pop_back();
			    break;
			 }
		     }
		  // add tag to storage
		  } else {
	             if (tagNest=="") {
			tagNest += buff;
		     } else {
		        tagNest += "."+buff;
		     }
		  }
	          tagList[ii] = tagNest;
	          buff = "";
	          break;
	       } else {
	          continue;
	       }
	    }

	    // get attribute name
	    if (!tagFlag && !attrValFlag && s!=' ') {
	       if (s!='=') {
		  buff+=s;
	       } else {
		  attrNameList[ii].push_back(buff);
		  buff = "";
		  attrValFlag = true;
		  skipSpace = true;
		  continue;
	       }
	    }

	    // get attribute value
	    if (!tagFlag && attrValFlag && !skipSpace) {
	       if (s!=' ' && s!='>' && s!='"') {
	          buff += s;
	       } else if (s==' ') {
		  attrValList[ii].push_back(buff);
		  buff = "";
		  attrValFlag = false;
	       } else if (s=='>') {
		  attrValList[ii].push_back(buff);
		  buff = "";
		  attrValFlag = false;
		  tagFlag = true;
	       }
	    } else {
	       skipSpace = false;
	    }
	}
    }



    // process queries
    for (int iq=0; iq<nQ; ++iq) {
	// get line
	string str {""};
        getline(cin,str);

	// get tag, attribute from query
	string tagQuery {""};
	string attrName {""};
	bool tagFlag {true};
	for (auto s : str) {
	    if (tagFlag) {
	       if (s!='~') {
	          tagQuery+=s;
	       } else {
	          tagFlag = false;
		  continue;
	       }
	    } else {
	       attrName += s;
	    }
	}

	// retrieve attribute value for query
	// check tag of query
	bool checkTag {false};
	int tagIndex {0};
	for (int jj=0; jj<nMarkup; ++jj) {
	    if (tagList[jj]==tagQuery) {
	       tagIndex = jj;
	       checkTag = true;
	       break;
	    }
	}

	// check attribute of query
	bool checkAttr {false};
	int attrIndex {0};
	if (checkTag) {
	   for (int jj=0; jj<attrNameList[tagIndex].size(); ++jj) {
	       if (attrNameList[tagIndex][jj]==attrName) {
	          attrIndex = jj;
		  checkAttr = true;
	          break;
	       }
	   }
	}

	// print result of query
	if (checkTag && checkAttr) {
	   cout << attrValList[tagIndex][attrIndex] << endl;
	} else {
	   cout << "Not Found! " << endl; 
	}
	
    }
    
    
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
