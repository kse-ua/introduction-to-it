#include <iostream>
#include <vector>

using namespace std;

pair<int, int> first_and_last(vector<int>& vec)
{
    pair<int, int> f_l;
    f_l.first = vec.front();
    f_l.second = vec.back();
    return f_l;
}

int main()
{
    vector<int> vector = { 0, 10, 5, 4 ,3 };

    pair<int, int> f_l = first_and_last(vector);

    cout << f_l.first << " " << f_l.second;
}

