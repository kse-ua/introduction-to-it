
#include <iostream>
#include <string>
#include <boost/algorithm/string.hpp>

using namespace std;

int main(int argc, const char* argv[]){

    std::vector<std::string> cities{"Athens", "Roma"};

    cout << "cities:  ['Athens', 'Roma']" << endl;
    auto func = [&](vector<string> cities_list) {
        cout <<  "[ ";
        for (std::string city: cities_list) {
            boost::to_upper(city);
            cout << "'" << city << "'" << " ";
        }
        cout <<  "]" << endl;
    };

    func(cities);

    cout << "cities:  ['Athens', 'Roma']" << endl;
    auto func_1 = [&](vector<string> cities_list) {
        cout <<  "[ ";
        for (std::string city: cities_list) {
            boost::to_lower(city);
            cout << "'" << city << "'" << " ";
        }
        cout <<  "]" << endl;
    };

    func_1(cities);

    std::vector<std::string> cities_2{"London", "Beijing", "Kiev"};
    
    cout << "cities:  ['London', 'Beijing', 'Kiev']" << endl;
    func(cities_2);

    auto len = [&](vector<string> cities_list) {
        cout <<  "[ ";
        for (std::string city: cities_list) {
            cout << city.size() << " ";
        }
        cout <<  "]" << endl;
    };

    std::vector<std::string> all_cities{"Athens", "Roma", "London", "Beijing", "Kiev", "Riga"};
    len(all_cities);

    return 0;

}



