#include<iostream>
#include<queue>

using namespace std;

void main()
{
	queue<int> MyQ;
	queue<pair<char, int>> MyQpair; //pair as underlying type

	MyQ.push(1);
	MyQ.push(2);
	MyQ.push(3);
	MyQ.push(4);

	MyQpair.push(pair<char, int>('a', 1));
	MyQpair.push(pair<char, int>('b', 2));
	MyQpair.push(pair<char, int>('c', 3));
	MyQpair.push(pair<char, int>('d', 4));
	MyQpair.push(pair<char, int>('e', 5));

	size_t Qsize = MyQ.size();

	cout << "MyQ:\n";
	for (int i = 0; i < Qsize; i++)
	{
		cout << MyQ.front() << '\n';
		MyQ.pop();
	}

	Qsize = MyQpair.size();

	cout << "MyQpair:\n";

	for (int i = 0; i < Qsize; i++)
	{
		cout << "(" << MyQpair.front().first << ", " << MyQpair.front().second << ")" << '\n';
		MyQpair.pop();
	}
}