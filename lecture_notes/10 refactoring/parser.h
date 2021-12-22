//
// Created by Stanislav Kramar on 12/20/21.
//

#ifndef JSONLIB_JSON_H
#define JSONLIB_JSON_H

#include <cstddef>
#include <map>
#include <string>
#include <variant>
#include <vector>

#include "json_exception.h"
#include "constants.h"
#include "json.h"

#ifndef DEBUG

#include <iostream>

#endif

namespace json {

    class parser {
    private:
        using special_value = std::variant<nullptr_t, bool, double>;

        std::string json_string;
        size_t index = 0;
        size_t line = 1;
        static const size_t ERROR_BUFFER_SIZE = 256;
        char *error_message = new char[ERROR_BUFFER_SIZE];
        const std::vector<char> whitespaces{' ', '\n', '\t', '\r'};


        void skip_whitespaces(bool raise_if_eof = false);

        void throw_json_error(const std::string &s);

        special_value parse_special_value(special_value value, const std::string &token);

        std::variant<int, double> parse_double_or_int();

        char parse_escape_sequence(char symbol);

        std::shared_ptr<json> parse_json(bool root = false);

        std::map<std::string, std::shared_ptr<json>> parse_object();

        std::vector<std::shared_ptr<json>> parse_list();

        std::string parse_string();

        bool parse_true();

        bool parse_false();

        std::nullptr_t parse_null();

        double parse_infinity();

        double parse_negative_infinity();

        double parse_nan();

        // TODO: Extend to support unbounded ints and long doubles.
        std::variant<int, double> parse_number();

    public:
        explicit parser(const std::string &s);

        ~parser();

        std::shared_ptr<json> parse();
    };

}
#endif //JSONLIB_JSON_H
