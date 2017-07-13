#include<iostream>
#include<map>

using namespace std;

void main()
{
	map<char, int> MyMap;

	MyMap.insert(MyMap.begin(), pair<char, int>('d', 1));
	MyMap.insert(MyMap.begin(), pair<char, int>('b', 2));
	MyMap.insert(MyMap.begin(), pair<char, int>('a', 3));
	MyMap.insert(MyMap.begin(), pair<char, int>('c', 4));

	auto it = MyMap.insert(pair<char, int>('e', 5)); //single element version returns false as pair::second if element exists

	if (it.second == false)
	{
		cout << "Element exist\n";
	}
	{
		cout << "Element inserted\n";
	}

	pair<map<char,int>::iterator,bool> at = MyMap.insert(pair<char, int>('f', 4));

	if (at.second == false)
	{
		cout << "Element exist\n";
	}
	{
		cout << "Element inserted\n";
	}

	cout << MyMap.at('e') << '\n';
	MyMap.erase('e');

	map<char, int> NewMap;

	MyMap.swap(NewMap);

	for (auto it = NewMap.begin(); it != NewMap.end(); it++)
	{
		cout << it->first << it->second << '\n';
	}

}