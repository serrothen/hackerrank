#include <iostream>
#include <iterator>

// comparison of zero initialization of static contiguous multidimensional arrays
// and ragged arrays of pointers
//
// Pro of static multidimensional array:
// *contiguous in memory [1]
// *can use foreach loop/iterators in contrast to ragged arrays [2]
// Contra:
// *size has to be fixed at compile time
//
// Pro of ragged array:
// *pointers can be relocated [3]
// *can allow for differently sized subarrays [4]
// *memory is saved if the subarrays are of different size [3]
// *memory has to be explicitely free'd [4]
// *size can be specified dynamically
//
// Contra of variable length array:
// *not part of C++ standard
// *only part of C99 standard
// *only few compilers have extension
//
// [1] https://nullprogram.com/blog/2016/10/27/
// [2] https://stackoverflow.com/questions/70997798/foreach-loop-in-pointer-arrays-in-c
// [3] https://stackoverflow.com/questions/23190858/array-of-pointers-vs-multidimensional-array
// [4] https://stackoverflow.com/questions/17823058/difference-between-multi-dimensional-arrays-and-array-of-pointers

void init(int ****arr,int size1,int size2,int size3) {

	(*arr) = new int**[size1];
	for (int ii=0; ii<size1; ++ii) {
		(*arr)[ii] = new int*[size2];
		for (int jj=0; jj<size2; ++jj) {
			(*arr)[ii][jj] = new int[size3];
			for (int kk=0; kk<size3; ++kk) {
				std::cout << ii << "," << jj << "," << kk << ": " << (*arr)[ii][jj][kk] << std::endl;
			}
		}
	}
}

void rem(int ****arr,int size1,int size2,int size3) {

	for (int ii=0; ii<size1; ++ii) {
		for (int jj=0; jj<size2; ++jj) {
			for (int kk=0; kk<size3; ++kk) {
				std::cout << ii << "," << jj << "," << kk << ": " << (*arr)[ii][jj][kk] << std::endl;
			}
			delete [] (*arr)[ii][jj];
		}
		delete [] (*arr)[ii];
	}
	delete [] (*arr);
	(*arr) = NULL;
}

int main() {

//        int size = 0;
//	scanf("%d",&size);

        // initializei variable size multidimensional array with zeros
	// via empty initializer list
//	int arr1[size][size] {};

	// output variable size multidimensional array
//	for (int ii=0; ii<size; ++ii) {
//		for (int jj=0; jj<size; ++jj)
//			std::cout << arr1[ii][jj] << " ";
//	std::cout << std::endl;
//	}
	// can use foreach loop
//	for (int (&el1)[5] : arr1) {
//		for (const int &el2 : el1)
//			std::printf("%d ", el2);
//	        std::printf("\n");
//	}

	// initialize array of pointers (ragged array)
	// via new (requires explicit "free" of memory)
//	int **arr2;
//	arr2 = new int*[size];
//	for (int ii=0; ii<size; ii++)
//		arr2[ii] = new int[size];

	// output ragged array (cannot use foreach loop)
//	for (int ii=0; ii<size; ++ii) {
//		for (int jj=0; jj<size; ++jj)
//			std::cout << arr2[ii][jj] << " ";
//	std::cout << std::endl;
//	}

//	delete[] arr2;

	std::cout << "arr3" << std::endl;
	int ***arr3;
	init(&arr3,5,5,5);
	for (int ii=0; ii<5; ++ii) {
		for (int jj=0; jj<5; ++jj) {
			for (int kk=0;kk<5; ++kk) {
			std::cout << ii << "," << jj << "," << kk << ": " << arr3[ii][jj][kk] << " ";
			}
		}
	std::cout << std::endl;
	}
	//rem(&arr3,5,5,5);

	if (arr3==NULL) {
		printf("NULL!!!");
	} else {
		printf("NOT NULL!!!");
	}

	int size1 = 5;
	int size2 = 5;
	int size3 = 5;
	int*** arr4 = new int**[size1];
	for (int ii=0; ii<size1; ii++) {
		arr4[ii] = new int*[size2];
		for (int jj=0; jj<size2; jj++) {
			arr4[ii][jj] = new int[size3];
			for (int kk=0; kk<size3; ++kk) {
				std::cout << ii << "," << jj << "," << kk << ": " << arr4[ii][jj][kk] << std::endl;
			}
		}
	}

	return 0;


}
