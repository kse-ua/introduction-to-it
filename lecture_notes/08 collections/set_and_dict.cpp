#include <iostream>
#include <set>
#include <map>

using namespace std;

void output_set()
{
    set<int> set;
    set.insert({ 0, 1, 2, 3, 4, 5 });

    auto x = set.find(0);
    auto y = set.find(5);

    cout << *x << " " << *y << "\n";
}

void output_dictionary()
{
    map<int, string> dict = {
        {1, "hello"},
        {2, "teacher"}
    };

    for (auto i = dict.cbegin(); i != dict.cend(); i++)
    {
        cout << i->first << " " <<  i->second << "\n";
    }
}

int main()
{
    output_set();

    output_dictionary();
}
