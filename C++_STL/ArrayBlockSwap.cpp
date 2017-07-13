#include<iostream>
#include<vector>
#include<queue>

using namespace std;

void main()
{
	vector<int> array;
	queue<int> myqueue;
	int temp, n, i, j;
	vector<int>::iterator it;

	cout << "Enter the size of the array\n";
	cin >> n;
	cout << "Enter the elements\n";

	for (i = 0; i < n; i++)
	{
		cin >> temp;
		array.push_back(temp);
	}

	/*for (it = array.begin(); it < array.end(); it++)
	{
		cout << *it << "\n";
	}*/

	cout << "Enter the index to split array at: ";
	cin >> temp;

	for (i = 0; i < temp; i++)
	{
		myqueue.push(array[i]);
	}

	for (j = 0, i = temp; i < array.size(); i++, j++)
	{
		array[j] = array[i];
	}

	for (i = j; !myqueue.empty(); i++)
	{
		array[i] = myqueue.front();
		myqueue.pop();
	}

	for (it = array.begin(); it < array.end(); it++)
	{
	cout << *it << "\n";
	}
}