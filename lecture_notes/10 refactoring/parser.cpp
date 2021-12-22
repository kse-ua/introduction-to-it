//
// Created by Stanislav Kramar on 12/20/21.
//

#include "parser.h"
#include "json.h"

#include <algorithm>
#include <cmath>
#include <cstdio>

std::shared_ptr<json::json> json::parser::parse() {
    skip_whitespaces();
    return parse_json(true);
}

json::parser::~parser() {
    delete[] error_message;
}

json::parser::parser(const std::string &s) {
    json_string = s;
}

std::shared_ptr<json::json> json::parser::parse_json(bool root) {
    skip_whitespaces();
    char first_symbol = json_string[index];
    std::shared_ptr<json> json_tree(new json);

    switch (first_symbol) {
        case OPEN_BRACE:
            json_tree->data = parse_object();
            break;
        case OPEN_SQUARE_BRACKET:
            json_tree->data= parse_list();
            break;
        case DOUBLE_QUOTE:
            json_tree->data = parse_string();
            break;
        case LOOKAHEAD_TRUE:
            json_tree->data = parse_true();
            break;
        case LOOKAHEAD_FALSE:
            json_tree->data = parse_false();
            break;
        case LOOKAHEAD_NULL:
            json_tree->data = parse_null();
            break;
        default:
            auto number = parse_number();
            try {
                json_tree->data = std::get<int>(number);
            }
            catch (std::bad_variant_access const &) {
                json_tree->data = std::get<double>(number);
            }

    }

    skip_whitespaces(root);
    return json_tree;
}

std::map<std::string, std::shared_ptr<json::json>> json::parser::parse_object() {
    skip_whitespaces();
    if (json_string[index] != OPEN_BRACE) {
        throw_json_error("Expecting value");
    }
    index += 1;
    skip_whitespaces();
    std::map<std::string, std::shared_ptr<json>> object;
    while (json_string[index] != CLOSING_BRACE) {
        std::string key = parse_string();
        skip_whitespaces();
        if (json_string[index] == COLON) {
            index += 1;
        } else {
            throw_json_error("Expecting ':' delimiter");
        }
        skip_whitespaces();

        auto value = parse_json();
        if (json_string[index] == COMMA) {
            index += 1;
            skip_whitespaces();
        } else if (json_string[index] == CLOSING_BRACE) {
            // left blank intentionally
        } else {
            throw_json_error("Expecting ',' delimiter");
        }

        object.insert({key, value});
    }

    if (json_string[index] == CLOSING_BRACE) {
        index += 1;
    }

    return object;
}

std::vector<std::shared_ptr<json::json>> json::parser::parse_list() {
    skip_whitespaces();
    if (json_string[index] != OPEN_SQUARE_BRACKET) {
        throw_json_error("Expecting value");
    }
    index += 1;
    skip_whitespaces();

    std::vector<std::shared_ptr<json>> list;

    while (json_string[index] != CLOSING_SQUARE_BRACKET) {

        skip_whitespaces();
        std::shared_ptr<json> element = parse_json();
        skip_whitespaces();
        list.push_back(element);
        if (json_string[index] == COMMA) {
            index += 1;
            skip_whitespaces();
        } else if (json_string[index] == CLOSING_SQUARE_BRACKET) {
        } else {
            throw_json_error("Expecting ',' delimiter");
        }
    }

    if (json_string[index] == CLOSING_SQUARE_BRACKET) {
        index += 1;
    }

    return list;
}

std::string json::parser::parse_string() {
    skip_whitespaces();
    if (json_string[index] != DOUBLE_QUOTE) {
        throw_json_error("Expecting value");
    }
    index += 1;

    std::string s;
    char current;
    while (json_string[index] != DOUBLE_QUOTE) {
        current = json_string[index];
        if (current == LOOKAHEAD_ESCAPE_BACKSLASH) {
            index += 1;
            current = parse_escape_sequence(json_string[index + 1]);
        }
        s += current;
        index += 1;
        if (index == json_string.length()) {
            throw_json_error("Unterminated string starting at");
        }
    }
    index += 1;
    return s;
}

bool json::parser::parse_true() {
    skip_whitespaces();
    return std::get<bool>(parse_special_value(true, JSON_TRUE));
}

bool json::parser::parse_false() {
    skip_whitespaces();

    return std::get<bool>(parse_special_value(false, JSON_FALSE));
}

std::nullptr_t json::parser::parse_null() {
    skip_whitespaces();
    return std::get<std::nullptr_t>(parse_special_value(nullptr, JSON_NULL));
}

double json::parser::parse_infinity() {
    skip_whitespaces();
    return std::get<double>(parse_special_value(INFINITY, JSON_INFINITY));
}

double json::parser::parse_negative_infinity() {
    return -parse_infinity();
}

double json::parser::parse_nan() {
    skip_whitespaces();
    return std::get<double>(parse_special_value(std::nan(JSON_NAN), JSON_NAN));
}

std::variant<int, double> json::parser::parse_number() {
    skip_whitespaces();
    char current = json_string[index];
    switch (current) {
        case LOOKAHEAD_INFINITY:
            return parse_infinity();
        case LOOKAHEAD_NAN:
            return parse_nan();
        default:
            if (current == LOOKAHEAD_MINUS) {
                if (json_string[index + 1] == LOOKAHEAD_INFINITY) {
                    index += 1;
                    return parse_negative_infinity();
                } else {
                    return parse_double_or_int();
                }
            } else
                return parse_double_or_int();
    }
}

char json::parser::parse_escape_sequence(char symbol) {
    switch (symbol) {
        case LOOKAHEAD_ESCAPE_NEWLINE:
            return '\n';
        case LOOKAHEAD_ESCAPE_TAB:
            return '\t';
        case LOOKAHEAD_ESCAPE_CARRIAGE_RETURN:
            return '\r';
        case LOOKAHEAD_ESCAPE_BACKSLASH:
            return '\\';
        default:
            throw_json_error("Invalid \\escape");
    }
}

std::variant<int, double> json::parser::parse_double_or_int() {
    std::vector<char> delimiters{',', '}', ']', ' ', '\n', '\t', '\r'};
    std::string number;
    bool use_double_parser = false;
    number.reserve(16);
    char current;
    while (std::find(delimiters.begin(), delimiters.end(), json_string[index]) == delimiters.end()) {
        current = json_string[index];
        if (current == DECIMAL) {
            use_double_parser = true;
        }
        number += current;
        index += 1;
    }

    try {
        if (use_double_parser) {
            return std::stod(number);
        } else {
            return std::stoi(number);
        }
    }
    catch (std::invalid_argument const &e) {
        throw_json_error("Extra data");
    }

}

json::parser::special_value json::parser::parse_special_value(parser::special_value value, const std::string &token) {
    size_t token_length = token.length();
    if (json_string.substr(index, token_length) == token) {
        index += token_length;
        return value;
    } else
        throw_json_error("Expecting value");
}

void json::parser::throw_json_error(const std::string &s) {
    size_t column = index / line + 1;
    snprintf(
            error_message,
            ERROR_BUFFER_SIZE,
            "JSONError: %s: line %zu column %zu (char %zu)",
            s.c_str(), line, column, index
    );
    throw json_exception(error_message);
}

void json::parser::skip_whitespaces(bool raise_if_eof) {
    while (std::find(whitespaces.begin(), whitespaces.end(), json_string[index]) != whitespaces.end()) {
        if (json_string[index] == '\n')
            line += 1;
        index += 1;
    }
    if (raise_if_eof && index > json_string.length())
        throw_json_error("Extra data");
}
