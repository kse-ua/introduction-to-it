//
// Created by Stanislav Kramar on 12/20/21.
//

#ifndef JSONLIB_CONSTANTS_H
#define JSONLIB_CONSTANTS_H

#define JSON_NULL "null"
#define JSON_TRUE "true"
#define JSON_FALSE "false"
#define JSON_INFINITY "Infinity"
#define JSON_NAN "NaN"

enum LOOKAHEAD_SYMBOLS : char {
    OPEN_BRACE = '{',
    CLOSING_BRACE = '}',
    COLON = ':',
    COMMA = ',',
    DECIMAL = '.',
    OPEN_SQUARE_BRACKET = '[',
    CLOSING_SQUARE_BRACKET = ']',
    DOUBLE_QUOTE = '"',
    LOOKAHEAD_TRUE = 't',
    LOOKAHEAD_FALSE = 'f',
    LOOKAHEAD_NULL =  'n',
    LOOKAHEAD_INFINITY = 'I',
    LOOKAHEAD_NAN = 'N',
    LOOKAHEAD_MINUS = '-',
    LOOKAHEAD_ESCAPE_NEWLINE = 'n',
    LOOKAHEAD_ESCAPE_TAB = 't',
    LOOKAHEAD_ESCAPE_CARRIAGE_RETURN = 'r',
    LOOKAHEAD_ESCAPE_BACKSLASH = '\\'
};

#endif //JSONLIB_CONSTANTS_H
