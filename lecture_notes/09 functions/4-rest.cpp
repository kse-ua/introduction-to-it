#include <iostream>
#include <map>

#ifndef _WIN32

#include <cxxabi.h>

#endif

using namespace std;

void catch_rest() {
    cout << endl; // handle recursion base case
}


template<typename T, typename ...Types>
void catch_rest(T arg, Types ...args) {
    cout << arg << " ";
    catch_rest(args...);
}


void print_variable_type_and_value() {} // left blank intentionally to handle base case

template<typename T, typename ...Types>
void print_variable_type_and_value(T arg, Types ...args) {
    const auto& arg_typename = typeid(T).name();
#ifdef _WIN32 // on msvc, typeid(T).name() returns a readable name while on gcc/clang the name is mangled
    cout << "Type: " << arg_typename << endl;
#else
    // so here I use an ABI function to demangle typename
    cout << "Type: " << abi::__cxa_demangle(arg_typename, 0, 0, 0) << endl;
#endif

    cout << "Value: ";

    if constexpr(is_same<T, map<string, string>>::value) {
        auto print_map = [](const T& m) {
            cout << "{" << endl;
            for (const auto& kv : m) {
                cout << "\t" << kv.first << ": " << kv.second << endl;
            }
            cout << "}";
        };
        print_map(arg);
    } else {
        cout << arg;
    }

    cout << endl;
    print_variable_type_and_value(args...);
}


int main() {
    catch_rest(1, 2, 3);
    print_variable_type_and_value(1, "Marcus", map<string, string> {{"field", "value"}});
    return 0;
}
