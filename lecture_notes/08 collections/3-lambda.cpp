#include <iostream>
#include <vector>
using namespace std;

vector<int> vec = { 0, 4, 5, 1 };

void first()
{
	cout << vec.front() << " ";
}

void last()
{
	cout << vec.back() << " ";
}

int main()
{
	vector<int> vec = { 0, 4, 5, 1 };

	auto out = []() {first(); last(); };
	out();
}