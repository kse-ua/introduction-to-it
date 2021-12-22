//
// Created by Stanislav Kramar on 12/20/21.
//

#include "json_exception.h"

#include <utility>

json::json_exception::json_exception(const char *message) : msg_(message) {}

json::json_exception::json_exception(std::string message) : msg_(std::move(message)) {}

const char *json::json_exception::what() const noexcept {
    return msg_.c_str();
}
