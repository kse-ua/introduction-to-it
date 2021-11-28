#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;

using DataSetValue = map<string, string>;

void print_map(const DataSetValue& m) {
    cout << "Map: { ";
    for (const auto& kv : m) {
        cout << kv.first << " = " << kv.second << " ";
    }
    cout << "}" << endl;
}

void print_dataset(const vector<DataSetValue>& v) {
     cout << "[ " << endl;
     for (const auto& m : v) {
        cout << "\t";
        print_map(m);
     }
     cout << "]" << endl;
}

vector<DataSetValue> distinct(const vector<DataSetValue>& dataset) {
    map<string, DataSetValue> dataset_map;
    for (const auto& record : dataset) {
        string key;
        for (const auto& kv : record) {
            key += kv.second;
        }
        if (dataset_map.find(key) == dataset_map.end())
            dataset_map.insert({key, record});
    }

    size_t size = dataset_map.size();
    vector<DataSetValue> distinct_dataset(size);
    auto it = dataset_map.begin();
    for (size_t i = 0; i < size; ++i) {
        distinct_dataset[i] = (*it).second;
        it++;
    }

    return distinct_dataset;
}

int main() {
    vector<DataSetValue> flights {
        {{"from", "Kiev"}, {"to", "Rome"}},
        {{"from", "Kiev"}, {"to", "Warsaw"}},
        {{"from", "Dublin"}, {"to", "Riga"}},
        {{"from", "Riga"}, {"to", "Dublin"}},
        {{"from", "Kiev"}, {"to", "Rome"}},
        {{"from", "Cairo"}, {"to", "Paris"}}
    };
    print_dataset(flights);

    auto directions = distinct(flights);
    print_dataset(directions);

    return 0;
}
