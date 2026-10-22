# Yacc example

from calclex import tokens
from ply import yacc

precedence = (
    ("left", "OR"),
    ("left", "AND"),
    ("right", "NOT", "NEGATIVE"),
    ("right", "EQUALS"),
    ("left", "PLUS", "MINUS"),
    ("left", "TIMES", "DIVIDE"),
    ("left", "LPAREN", "RPAREN"),
)

variables = {}


def p_statement(p):
    """statement : statement expression
    | expression"""
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = p[1]


def p_assign_expr(p):
    "expression : ID EQUALS expression"
    variables[p[1]] = p[3]
    p[0] = p[3]


def p_expression(p):
    """expression : expression PLUS term
    | expression MINUS term
    | term"""
    if len(p) < 3:
        p[0] = p[1]
    elif p[2] == "+":
        p[0] = p[1] + p[3]
    elif p[2] == "-":
        p[0] = p[1] - p[3]


def p_term(p):
    """term : term TIMES factor
    | term DIVIDE factor"""
    if p[2] == "*":
        p[0] = p[1] * p[3]
    elif p[2] == "/":
        p[0] = p[1] / p[3]


def p_term_and(p):
    "term : factor AND term"
    p[0] = bool(p[1] and p[3])


def p_term_or(p):
    "term : factor OR term"
    p[0] = bool(p[1] or p[3])


def p_term_not(p):
    "term : NOT term"
    p[0] = bool(not p[2])


def p_expression_negative(p):
    "expression : MINUS expression"
    p[0] = - p[2]


def p_term_factor(p):
    "term : factor"
    p[0] = p[1]


def p_factor_num(p):
    "factor : NUMBER"
    p[0] = p[1]


def p_factor_expr(p):
    "factor : LPAREN expression RPAREN"
    p[0] = p[2]


def p_factor_id(p):
    "factor : ID"
    p[0] = variables[p[1]]


def p_error(p):
    print("Syntax error in input!")


# def p_empty(p):
#    "empty :"


# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input("calc > ")
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    print(result)
