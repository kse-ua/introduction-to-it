#include <iostream>
#include <vector>
#include <string>

using namespace std;

void faster_out(vector<int>& vec)
{
    string s = "";

    for (int i = 0; i < vec.size(); i++)
    {
        s += to_string(vec[i]) + " ";
    }

    cout << s;
}

int main()
{
    vector<int> first = { 0, 1, 1, 5, 2 };
    vector<int> second = { 1, 2, 3, 4 }; // lets use our first vector after concat

    for (int i = 0; i < second.size(); i++)
    {
        first.push_back(second[i]);
    }

    faster_out(first);
}