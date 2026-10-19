# Yacc example

from calclex import tokens
from ply import yacc

start = "or_expr"


def p_or_expr(p):
    "or_expr : or_expr OR and_expr"
    p[0] = bool(p[1] or p[3])


def p_or_expr_and(p):
    "or_expr : and_expr"
    p[0] = p[1]


def p_and_expr(p):
    "and_expr : and_expr AND not_expr"
    p[0] = bool(p[1] and p[3])


def p_and_expr_not(p):
    "and_expr : not_expr"
    p[0] = p[1]


def p_not_expr(p):
    "not_expr : NOT not_expr"
    p[0] = not p[2]


def p_not_expr_expression(p):
    "not_expr : expression"
    p[0] = p[1]


def p_expression(p):
    """expression : expression PLUS term
    | expression MINUS term"""
    if p[2] == "+":
        p[0] = p[1] + p[3]
    elif p[2] == "-":
        p[0] = p[1] - p[3]


def p_expression_term(p):
    "expression : term"
    p[0] = p[1]


def p_term(p):
    """term : term TIMES factor
    | term DIVIDE factor"""
    if p[2] == "*":
        p[0] = p[1] * p[3]
    elif p[2] == "/":
        p[0] = p[1] / p[3]


def p_term_factor(p):
    "term : factor"
    p[0] = p[1]


def p_factor_num(p):
    "factor : NUMBER"
    p[0] = p[1]


def p_factor_paren(p):
    "factor : LPAREN or_expr RPAREN"  # was: LPAREN expression RPAREN
    p[0] = p[2]


def p_factor_expr(p):
    "factor : LPAREN expression RPAREN"
    p[0] = p[2]


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
