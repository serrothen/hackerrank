#include<bits/stdc++.h>

using namespace std;

//Implement the class Box  
//l,b,h are integers representing the dimensions of the box

// The class should have the following functions : 

// Constructors: 
// Box();
// Box(int,int,int);
// Box(Box);


// int getLength(); // Return box's length
// int getBreadth (); // Return box's breadth
// int getHeight ();  //Return box's height
// long long CalculateVolume(); // Return the volume of the box

//Overload operator < as specified
//bool operator<(Box& b)

//Overload operator << as specified
//ostream& operator<<(ostream& out, Box& B)

class Box {
  // properties are private
  int l,b,h;
  
  // methods are public
  public:
  
  // default constructor
  Box();
  // constructor with arguments
  Box(const int& length, const int& breadth, const int& height);
  // copy constructor
  Box(const Box&);
  
  // getters
  int getLength();
  int getBreadth();
  int getHeight();

  // method
  long CalculateVolume();
  
  // operator overloads
  bool operator < (const Box&) const;
  // "friend" needed to allow access to private properties
  // for non-member function
  friend std::ostream& operator << (std::ostream&, const Box&);
};

Box::Box() {
    l = 0;
    b = 0;
    h = 0;
}

Box::Box(const int& length, const int& breadth, const int& height) {
    l = length;
    b = breadth;
    h = height;
}

Box::Box(const Box& box) {
    l = box.l;
    b = box.b;
    h = box.h;
}

int Box::getLength() {
    return l;
}

int Box::getBreadth() {
    return b;
}

int Box::getHeight() {
    return h;
}

long Box::CalculateVolume() {
    // explicit cast to long
    return (long)l*b*h;
}

bool Box::operator < (const Box& rhs) const {
    if ( (l<rhs.l) || (b<rhs.b && l==rhs.l) || (h<rhs.h && b==rhs.b && l==rhs.l) ) {
        return true;
    }
    return false;
}

// non-member function of Box
std::ostream& operator << (std::ostream& os, const Box& rhs) {
    return os << rhs.l << " " << rhs.b << " " << rhs.h;
}



void check2()
{
	int n;
	cin>>n;
	Box temp;
	for(int i=0;i<n;i++)
	{
		int type;
		cin>>type;
		if(type ==1)
		{
			cout<<temp<<endl;
		}
		if(type == 2)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			temp=NewBox;
			cout<<temp<<endl;
		}
		if(type==3)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			if(NewBox<temp)
			{
				cout<<"Lesser\n";
			}
			else
			{
				cout<<"Greater\n";
			}
		}
		if(type==4)
		{
			cout<<temp.CalculateVolume()<<endl;
		}
		if(type==5)
		{
			Box NewBox(temp);
			cout<<NewBox<<endl;
		}

	}
}

int main()
{
	check2();
}
