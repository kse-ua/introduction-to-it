#include <map>
#include <iostream>
#include <string>

using namespace std;

map<string, int> cache;

void sum(int a, int b)
{
    string key = to_string(a) + "," + to_string(b);

    map<string, int>::iterator i = cache.find(key);

    if (i != cache.end())
    {
        cout << i->second << "\n";
        // cout << "I was here!"; | you can uncomment this and check that program actually enters this statement for second sum call
    }

    else
    {
        cache.insert({ key, a + b });
        cout << a + b << "\n";
    }
}

void substract(int a, int b)
{
    string key = to_string(a) + "," + to_string(b);

    map<string, int>::iterator i = cache.find(key);

    if (i != cache.end())
    {
        cout << i->second << "\n";
        // cout << "I was here!"; | you can uncomment this and check that program actually enters this statement for second sum call
    }

    else
    {
        cache.insert({ key, a - b });
        cout << a - b << "\n";
    }
}

int main()
{
    sum(5, 2);
    substract(5, 2); // nothing changes, but with shared cache first entered value by key will be used for any next by order operation for this key
}