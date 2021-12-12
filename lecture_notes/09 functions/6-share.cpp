#include <stdio.h>
#include <map>
#include <string>

std::map<std::string, int> cache;

int addprocedure(int a, int b)
{

    std::string key = std::to_string(a) + "," + std::to_string(b);
    std::map<std::string, int>::iterator it = cache.find(key);

    if (it != cache.end())
    {
        return it->second;
    }
    int res = a + b;
    cache[key] = res;
    return res;
}

int subprocedure(int a, int b)
{
    std::string key = std::to_string(a) + "," + std::to_string(b);
    std::map<std::string, int>::iterator it = cache.find(key);

    if (it != cache.end())
    {
        return it->second;
    }
    int res = a - b;
    cache[key] = res;
    return res;
}

int main()
{
    printf("{ sub: %d }\n{ add: %d }", subprocedure(5, 2), addprocedure(5, 2));
}