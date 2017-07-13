#include<iostream>
#include<forward_list>
#include<queue>
#include<list>
#include <functional> //std::greater

using namespace std;

void main()
{
	forward_list<int> MyFlist;
	forward_list<queue<int>> MyFlist_list;

	MyFlist.push_front(1);
	MyFlist.push_front(2);
	MyFlist.push_front(3);
	MyFlist.push_front(4);

	MyFlist.insert_after(MyFlist.before_begin(), 0); //insert after, .before_begin()
	MyFlist.emplace_after(MyFlist.begin(), 10);  //emplace_after
	MyFlist.erase_after(MyFlist.begin());  //erase_after

	queue<int> a;
	MyFlist_list.push_front(a);


	MyFlist_list.front().push(10);
	MyFlist_list.front().push(20);
	MyFlist_list.front().push(30);
	MyFlist_list.front().push(40);

	size_t Qsize;
	for (auto it = MyFlist_list.begin(); it != MyFlist_list.end(); it++)
	{
		Qsize = it->size();		//Getting size of queue at 'it' position of MyFlist_list
		for (auto i = 0; i < Qsize; i++)
		{
			cout << it->front() << '\n';		//print queue at location pointed by 'it'
			it->pop();
		}
		
	}

	forward_list<int> Flist = { 100,200 };
	MyFlist.splice_after(MyFlist.begin(), Flist); //splice_after: add elements of Flist after begin() position of MyFlist and remove from Flist

	MyFlist.insert_after(MyFlist.begin(), 0);
	MyFlist.unique(); //remove element if it is equal to the element directly preceeding it

	MyFlist.sort(std::greater<int>()); //descending sorting order
}