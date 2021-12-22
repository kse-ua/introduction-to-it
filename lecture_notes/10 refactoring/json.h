//
// Created by Stanislav Kramar on 12/21/21.
//

#ifndef JSON_JSON_H
#define JSON_JSON_H

#include <map>
#include <memory>
#include <string>
#include <variant>
#include <vector>

namespace json {

    class json {
    public:
        std::variant<bool, int, double, std::nullptr_t, std::string, std::map<std::string, std::shared_ptr<json>>, std::vector<std::shared_ptr<json>>> data;

        template<class T>
        T at(size_t index) {
            return std::get<T>(std::get<std::vector<std::shared_ptr<json>>>(data)[index]->data);
        }

        template<class T>
        T get(const std::string& key) {
            return std::get<T>(std::get<std::map<std::string, std::shared_ptr<json>>>(data)[key]->data);
        }
    };

    using pjson = std::shared_ptr<json>;
}
#endif //JSON_JSON_H
