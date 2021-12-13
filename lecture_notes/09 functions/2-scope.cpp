#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<string> vec = { "Athens", "Roma", "London", "Beijing", "Kiev", "Riga" };

void vec_to_cases(vector<string> &v, int direction, bool show_length)
{
    vector<string> vec_st2;
    string st = "";

    if (direction == 1)
    {
        for (int i = 0; i < v.size(); i++)
        {

            for (int j = 0; j < v[i].length(); j++)
            {
                st += toupper(v[i][j]);
            }

            vec_st2.push_back(st);
            st = "";
        }
    }

    else if (direction == 2)
    {
        for (int i = 0; i < v.size(); i++)
        {

            for (int j = 0; j < v[i].length(); j++)
            {
                st += tolower(v[i][j]);
            }

            vec_st2.push_back(st);
            st = "";
        }

    }

    else vec_st2 = vec;

    if (show_length == true)
    {
        cout << "(" << vec_st2.size() << ") ";

        for (int i = 0; i < vec_st2.size(); i++)
        {
            cout << vec_st2[i] << " ";
        }
    }

    else
    {
        for (int i = 0; i < vec_st2.size(); i++)
        {
            cout << vec_st2[i] << " ";
        }
    }
}

int main()
{
    vec_to_cases(vec, 1, true);
    /*
        1 parameter - your vector, which contains cities
        2 parameter - 1 to show in upper, 2 to show in lower, anything else from 3 to 2.147 * 10^9 (int limit) - keep w/o changes
        3 parameter - true to show length / false to show in lower
    */
}

/*
        or split code above to separate functions and use like -> show_length(is_default((show_upper(vec)))) and recombine upper/lower how you want to with manual vec changes
*/