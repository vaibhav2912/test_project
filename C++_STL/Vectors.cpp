#include<iostream>
#include<vector>
#include<list>
#include<queue>

using namespace std;

void main()
{
	vector<int> arr;
	priority_queue<int> prq;

	prq.push(5); 
	prq.push(1); 
	prq.push(7); 
	prq.push(8); 
	prq.push(10); 
	prq.push(12);

	arr.push_back(1); arr.push_back(2); arr.push_back(3); arr.push_back(4); arr.push_back(5); // 1 2 3 4 5

	int ls[] = { 10,20,30,40,50 }; // 10 20 30 40 50
	vector<int> arr1(ls, ls + 5);

	//arr.clear();

	cout << "Capacity = " << arr.capacity() << "\n Size = " << arr.size() << "\n";
	arr.shrink_to_fit();
	cout << "Shrink Capacity = " << arr.capacity() << "\n Size = " << arr.size() << "\n";
	bool a = arr.empty();

	vector<int>::iterator at;
	at = arr.begin();

	at = arr.insert(arr.begin(), 2, 300); // 300 300 1 2 3 4 5
	at = arr.insert(at + 1, 400); // 300 400 300 1 2 3 4 5

	vector<int>::iterator er = arr.begin() + 2;
	arr.erase(er);  // 300 400 1 2 3 4 5
	cout << ".IsEmpty = " << a << "\n";

	arr1.emplace(arr1.end(), 10); // 10 20 30 40 50 10
	arr.swap(arr1); // swap two vectors

	cout << "arr vector: \n";
	int* BeginPtr = arr.data();  //Using .data() for pointer to the start of underlying array
	size_t arrsize = arr.size();

	for (int i = 0; i < arrsize; i++)
	{
		cout << *BeginPtr << "\n";
		BeginPtr++;
	}

	cout << "arr vector again: \n";
	for (size_t i = 0; i < arrsize; i++)
	{
		cout << arr.back() << '\n';
		arr.pop_back();
	}

	vector<int>::iterator it;

	cout << "arr1 vector: \n";
	for (it = arr1.begin(); it < arr1.end(); it++)
	{
		cout << *it << "\n";
	}


	vector<int> arr1Copy;
	arr1Copy.assign(arr1.begin(), arr1.end()); //Constructor version

	vector<int>::const_reverse_iterator arrit;  //const reverse iterator

	cout << "arr1Copy in reverse: \n";
	for (arrit = arr1Copy.crbegin(); arrit < arr1Copy.crend(); arrit++)
	{
		cout << *arrit << '\n';
	}

	arr1Copy.erase(arr1Copy.begin() + 3);  //erase versions
	arr1Copy.emplace(arr1Copy.begin(), 22);  //emplace
	arr1Copy.emplace_back(11);  //emplace_back

	cout << "Erased copy \n";

	for (it = arr1Copy.begin(); it < arr1Copy.end(); it++)
	{
		cout << *it << '\n';
	}
}