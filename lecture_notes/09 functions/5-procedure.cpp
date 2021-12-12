#include <stdio.h>
#include <map>
#include <string>
int addfunction(int a, int b)
{
    int res = a + b;
    return res;
}

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
int main()
{
    printf("[%d, %d, %d, %d]\n",
           addfunction(10, 20),
           addfunction(1, 2),
           addfunction(100, 20),
           addfunction(100, 200)
           );

    printf("[%d, %d, %d, %d]\n",
           addprocedure(10, 20),
           addprocedure(1, 2),
           addprocedure(100, 20),
           addprocedure(100, 200)
           );
}
