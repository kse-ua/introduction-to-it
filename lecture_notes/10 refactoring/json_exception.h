//
// Created by Stanislav Kramar on 12/20/21.
//

#ifndef JSONLIB_JSON_EXCEPTION_H
#define JSONLIB_JSON_EXCEPTION_H

#include <exception>
#include <string>

namespace json {
    class json_exception : public std::exception {
    public:
        explicit json_exception(const char *message);

        explicit json_exception(std::string message);

        ~json_exception() noexcept override = default;

       [[nodiscard]] const char *what() const noexcept override;

    private:
        std::string msg_;
    };
}

#endif //JSONLIB_JSON_EXCEPTION_H
