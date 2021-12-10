#include <stdio.h>
float number = 228;
auto f = [](float num)
{ return num - 228; };

void f1()
{
    float number = 20;
    auto f = [](float num)
    { return num * 20; };

    printf("%f\n %f\n", number, f(number));
    {
        auto f = [](float num)
        { return num + 20; };

        printf("%f\n %f\n", number, f(number));
    }
    {
        float number = 25;

        printf("%f\n %f\n", number, f(number));
    }
}
int main()
{
    f1();
    printf("%f\n %f\n", number, f(number));
}
